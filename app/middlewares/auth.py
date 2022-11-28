from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.utils.env import env
from jose import JWTError, jwt, ExpiredSignatureError

oath2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)

async def check_token(token: str = Depends(oath2_scheme)):
    credentials_exception = lambda x : HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=x
    )
    try:
        payload = jwt.decode(token, env.SECRET_KEY, algorithms=[env.ALGORITHM])
        username: str = payload.get("sub")
    except ExpiredSignatureError:
        raise credentials_exception(str('Token has been expired'))
    except JWTError as error:
        raise credentials_exception(str(error))
    
    return username