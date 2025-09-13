from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
router = APIRouter(prefix="/users", tags=["Users"])
@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
 if db.query(models.User).filter_by(name=user.name).first():
  raise HTTPException(400, "User already exists")
 api_key = utils.generate_api_key()
 db_user = models.User(name=user.name, balance=user.balance,
api_key=api_key)
 db.add(db_user)
 db.commit()
 db.refresh(db_user)

 return db_user
@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
 user = db.query(models.User).get(user_id)
 if not user:
  raise HTTPException(404, "User not found")
 return user

# List all users (for frontend lookup)
@router.get("", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()