from datetime import datetime
import uuid 
from pydantic import BaseModel, EmailStr, constr

class UserSchema(BaseModel):
    id: uuid.UUID
    username: str 
    email: EmailStr
    
    class Config:
        orm_mode = True
        

class CreateUserSchema(UserSchema):
    password: constr(min_length=6)
    verified: bool = False

    
