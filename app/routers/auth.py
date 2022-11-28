from ..schemas import auth as schema
from ..models import user as model
from ..utils.database import get_db
from ..services import auth
from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.orm import Session
from passlib.hash import argon2

router = APIRouter()

@router.post('/login', status_code=status.HTTP_200_OK, response_model=schema.LoginResponseSchema)
def login(request: schema.LoginUserSchema,  db: Session = Depends(get_db)):
    existing_user = db.query(model.User).filter(model.User.email == request.email)
    user = existing_user.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User is not found')
    
    if not argon2.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Password not match')
    
    return schema.LoginResponseSchema(
        access_token=auth.generate_access_token(data={"sub": user.username}, expires_delta=1),
        expires_in=1
    )