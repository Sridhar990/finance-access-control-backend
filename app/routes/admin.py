from fastapi import HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from app.core.deps import require_admin
from app.models.user import User
from app.database import get_db




router=APIRouter(prefix="/admin",tags=["Admin"])

@router.get("/users")
def get_all_users(admin:User=Depends(require_admin),db:Session=Depends(get_db)):

    users=db.query(User).all()
    return users

#Admin disable user
@router.patch("/users/{user_id}/disable")
def disable_user(user_id:int,Admin:User=Depends(require_admin),db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if not user.is_active:
        return {"message":"user already disabled"}
    
    user.is_active=False
    db.commit()

    return {
        "message":"user disabled successfully"
    }


#Admin enable users
@router.patch("/users/{user_id}/enable")
def enable_user(
    user_id: int,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found")

    if user.is_active:
        return {"message": "User already active"}

    user.is_active = True
    db.commit()

    return {"message": "User enabled successfully"}

#admin delete user
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}






