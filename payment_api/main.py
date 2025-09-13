from fastapi import FastAPI
from .database import Base, engine
from .routes import users, payments
# create tables at startup (simple approach). In production, run migrations instead.
Base.metadata.create_all(engine)
app = FastAPI(title="Mini PayPal Clone - Production Ready")
app.include_router(users.router)
app.include_router(payments.router)