from datetime import datetime
import uuid 
from pydantic import BaseModel, EmailStr, constr

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=6)