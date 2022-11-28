from ..schemas import user as schema
from ..models import user as model
from ..utils.database import get_db
from ..middlewares.auth import check_token
from fastapi import Depends, status, APIRouter, HTTPException
from sqlalchemy.orm import session
from passlib.hash import argon2
import uuid 

router = APIRouter()

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=schema.UserSchema)
def create_user(request: schema.CreateUserSchema, db: session = Depends(get_db)):
    request.id = uuid.uuid4()
    request.password = argon2.hash(request.password)
    user = model.User(**request.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

@router.get('/me', response_model=schema.UserSchema)
def get_current_user(username: str = Depends(check_token), db: session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User is not found')
    
    return user
