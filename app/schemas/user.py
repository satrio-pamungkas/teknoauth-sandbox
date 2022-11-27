from typing import Union
import uuid 
from pydantic import BaseModel, EmailStr, constr

class UserSchema(BaseModel):
    id: Union [uuid.UUID, None] = None
    username: str 
    email: EmailStr
    
    class Config:
        orm_mode = True


class CreateUserSchema(UserSchema):
    password: constr(min_length=6)
    verified: bool = False
    
