from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    balance: float = 0.0
class UserOut(BaseModel):
 id: int
 name: str
 balance: float
 class Config:
        orm_mode = True
class PaymentCreate(BaseModel):
 payer_id: int
 payee_id: int
 amount: float
 currency: str = "USD"
class PaymentOut(BaseModel):
 id: int
 payer_id: int
 payee_id: int
 amount: float
 currency: str
 status: str
 created_at: datetime
 class Config:
    orm_mode = True
