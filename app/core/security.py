from passlib.context import CryptContext
from datetime import timedelta,datetime
from jose import jwt,JWTError
import os
from dotenv import load_dotenv

load_dotenv()


# password hashing 

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)



# JWT configuration HS256

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",30))

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is not set in enviroment variables")


# JWT helpers
def create_access_token(data:dict,expires_delta: timedelta | None=None):
    to_encode=data.copy()

    if expires_delta is not None:
        expire= datetime.utcnow() + expires_delta
    else:
        expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp":expire})

    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return token


# decode access token

def decode_access_token(token:str):
    try:
        playload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return playload

    except JWTError:
        return None
    










