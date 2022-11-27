from ..schemas import user as schema
from ..models import user as model
from ..utils.database import get_db
from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.orm import session
from passlib.hash import argon2
import uuid 

router = APIRouter()

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=schema.UserSchema)
def create_user(
    request: schema.CreateUserSchema, 
    db: session = Depends(get_db)
):
    request.id = uuid.uuid4()
    request.password = argon2.hash(request.password)
    user = model.User(**request.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user
