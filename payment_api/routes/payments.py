
from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from .. import schemas
from ..auth import get_current_user
from ..database import get_db
from ..services.payments_service import (
    PaymentError,
    cancel_payment as svc_cancel_payment,
    complete_payment as svc_complete_payment,
    create_payment as svc_create_payment,
    get_payment as svc_get_payment,
)
from ..tasks import send_payment_receipt_email

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=schemas.PaymentOut)
def create_payment(payment: schemas.PaymentCreate, x_idempotency_key: str = Header(None), db: Session = Depends(get_db)):
    current_user = get_current_user()
    # ensure the authenticated user is the payer
    if current_user.id != payment.payer_id:
        raise HTTPException(403, "API key does not belong to payer")
    try:
        pay = svc_create_payment(
            db, payment.payer_id, payment.payee_id,
            payment.amount, payment.currency, x_idempotency_key
        )
        db.commit()
        db.refresh(pay)
        return pay
    except PaymentError as e:
        raise HTTPException(400, str(e)) from e

@router.post("/{pid}/complete")
def complete_payment(pid: int, db: Session = Depends(get_db)):
    current_user = get_current_user()
    payment = svc_get_payment(db, pid)
    if not payment:
        raise HTTPException(404, "Payment not found")
    if payment.payer_id != current_user.id:
        raise HTTPException(403, "Only payer can complete this payment")
    try:
        pay = svc_complete_payment(db, pid)
        # trigger background receipt email
        try:
            send_payment_receipt_email.delay(pay.id)
        except Exception:
            # don't fail the request if Celery is down; log in real app
            pass
        db.commit()
        return {"message": "Payment completed"}
    except PaymentError as e:
        raise HTTPException(400, str(e)) from e

@router.post("/{pid}/cancel")
def cancel_payment(pid: int, db: Session = Depends(get_db)):
    current_user = get_current_user()
    payment = svc_get_payment(db, pid)
    if not payment:
        raise HTTPException(404, "Payment not found")
    if payment.payer_id != current_user.id:
        raise HTTPException(403, "Only payer can cancel this payment")
    try:
        svc_cancel_payment(db, pid)
        db.commit()
        return {"message": "Payment cancelled"}
    except PaymentError as e:
        raise HTTPException(400, str(e)) from e

@router.get("/{pid}", response_model=schemas.PaymentOut)
def get_payment(pid: int, db: Session = Depends(get_db)):
    current_user = get_current_user()
    pay = svc_get_payment(db, pid)
    if not pay:
        raise HTTPException(404, "Payment not found")
    # only payer or payee can fetch
    if current_user.id not in (pay.payer_id, pay.payee_id):
        raise HTTPException(403, "Forbidden")

    return pay
