from .celery_app import celery_app
from .database import SessionLocal
from .models import Payment, User

@celery_app.task(name='payment.send_receipt')
def send_payment_receipt_email(payment_id: int) -> bool:
	db = SessionLocal()
	try:
		payment = db.query(Payment).get(payment_id)
		if not payment:
			return False
		payer = db.query(User).get(payment.payer_id)
		payee = db.query(User).get(payment.payee_id)
		# In a real app you'd send a real email. Here we just simulate.
		print(f"[task] Sending receipt: payment={payment.id} from {payer.name} to {payee.name} amount={payment.amount} {payment.currency}")
		return True
	finally:
		db.close()