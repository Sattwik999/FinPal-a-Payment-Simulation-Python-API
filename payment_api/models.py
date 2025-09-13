from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
class User(Base):
 __tablename__ = "users"
 id = Column(Integer, primary_key=True)
 name = Column(String, unique=True, nullable=False)
 balance = Column(Float, default=0.0, nullable=False)
 api_key = Column(String, unique=True, index=True, nullable=False)
 payments_sent = relationship("Payment", foreign_keys='Payment.payer_id',
back_populates="payer")
 payments_received = relationship("Payment",
foreign_keys='Payment.payee_id', back_populates="payee")

class Payment(Base):
 __tablename__ = "payments"
 id = Column(Integer, primary_key=True)
 payer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
 payee_id = Column(Integer, ForeignKey("users.id"), nullable=False)
 amount = Column(Float, nullable=False)
 currency = Column(String(8), default="USD", nullable=False)
 status = Column(String(32), default="pending", nullable=False)
 created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
 updated_at = Column(DateTime, default=datetime.utcnow,
 onupdate=datetime.utcnow, nullable=False)
 idempotency_key = Column(String, unique=True, nullable=True)
 
 payer = relationship("User", foreign_keys=[payer_id],
 back_populates="payments_sent")
 
 payee = relationship("User", foreign_keys=[payee_id],
back_populates="payments_received")