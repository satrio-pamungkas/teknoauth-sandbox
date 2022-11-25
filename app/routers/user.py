from ..schemas import user as schema
from ..models import user as model
from ..utils.database import get_db
from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.orm import session
import uuid 

router = APIRouter()

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=schema.UserSchema)
def create_user(user: schema.CreateUserSchema, db: session = Depends(get_db)):
    user.id = uuid.uuid4()
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
