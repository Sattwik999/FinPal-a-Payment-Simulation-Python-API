from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models import User, Payment
from typing import Optional

class PaymentError(Exception):
    pass


def create_payment(db: Session, payer_id: int, payee_id: int, amount: float, currency: str = "USD", idempotency_key: Optional[str] = None) -> Payment:
    # idempotency check
    if idempotency_key:
        existing = db.query(Payment).filter_by(idempotency_key=idempotency_key).first()
        if existing:
            return existing

    # Transactional block - protect balances with SELECT ... FOR UPDATE
    try:
        with db.begin():
            payer = db.query(User).filter(User.id == payer_id).with_for_update().first()
            payee = db.query(User).get(payee_id)
            if not payer or not payee:
                raise PaymentError("Invalid payer or payee")
            if payer.balance < amount:
                raise PaymentError("Insufficient balance")

            payment = Payment(payer_id=payer_id, payee_id=payee_id, amount=amount, currency=currency, idempotency_key=idempotency_key)
            db.add(payment)
            # commit happens automatically by context manager
            return payment
    except IntegrityError as e:
        # could happen if idempotency key is duplicated
        db.rollback()
        raise PaymentError("Database integrity error")


def complete_payment(db: Session, payment_id: int) -> Payment:
    try:
        with db.begin():
            payment = db.query(Payment).get(payment_id)
            if not payment or payment.status != "pending":
                raise PaymentError("Invalid or non-pending payment")
            payer = db.query(User).filter(User.id == payment.payer_id).with_for_update().first()
            payee = db.query(User).get(payment.payee_id)
            if payer.balance < payment.amount:
                raise PaymentError("Insufficient balance")

            payer.balance -= payment.amount
            payee.balance += payment.amount
            payment.status = "completed"
            # return the payment object
            return payment
    except Exception:
        db.rollback()
        raise


def cancel_payment(db: Session, payment_id: int) -> Payment:
    with db.begin():
        payment = db.query(Payment).get(payment_id)
        if not payment or payment.status != "pending":
            raise PaymentError("Invalid or non-pending payment")
        payment.status = "cancelled"
        return payment


def get_payment(db: Session, payment_id: int) -> Optional[Payment]:
    return db.query(Payment).get(payment_id)