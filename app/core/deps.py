from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.core.security import decode_access_token
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):

    playload=decode_access_token(token)

    if playload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or Expired Token",headers={"WWW-Authentication":"bearer"})
    
    user_id=playload.get("sub")

    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token playload")
    

    user=db.query(User).filter(User.id==user_id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="user not found")
    
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="user is inactive")
    
    return user


# admin role deps

def require_admin(current_user:User=Depends(get_current_user)):
    if current_user.role!="ADMIN":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Admin access required")
    
    return current_user