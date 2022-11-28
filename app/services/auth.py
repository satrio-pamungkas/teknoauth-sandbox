from jose import JWTError, jwt 
from typing import Union
from datetime import datetime, timedelta
from app.utils.env import env

SECRET_KEY = env.SECRET_KEY
ALGORITHM = env.ALGORITHM

def generate_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    print(expires_delta)
    if expires_delta:
        expire = datetime.now() + timedelta(expires_delta)
    else:
        expire = datetime.now() + timedelta(minutes=10)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt