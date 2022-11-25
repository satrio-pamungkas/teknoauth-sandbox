from ..schemas import auth as schema
from ..models import user as model
from ..utils.database import get_db
from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.orm import Session
import uuid 

router = APIRouter()

@router.post('/login')
def login(request: schema.LoginUserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(model.User).filter(model.User.email == request.email)
    user = existing_user.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User is not found')
    
    if user.password != request.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Password not match')
    
    return Response(status_code=status.HTTP_200_OK)