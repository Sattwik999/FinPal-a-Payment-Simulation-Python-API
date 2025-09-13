from celery import Celery
from .config import get_settings
settings = get_settings()
celery_app = Celery("payment_api", broker=settings.REDIS_URL,
backend=settings.REDIS_URL)
# simple configuration - more tuning needed for production
celery_app.conf.update(task_serializer='json', accept_content=['json'],
result_serializer='json')
celery_app.conf.task_routes = {
    'payment_api.tasks.send_payment_receipt_email': {'queue': 'emails'},
}