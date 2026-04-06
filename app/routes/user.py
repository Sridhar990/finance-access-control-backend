
from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.core.deps import get_current_user
from app.models.user import User
from app.models.profile import Profile
from app.schemas.user import UserResponse
from app.schemas.auth import ChangePassword
from app.core.security import verify_password,hash_password
from app.schemas.profile import UpdateProfile
from app.database import get_db
from sqlalchemy.orm import joinedload



router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = (
        db.query(User)
        .options(joinedload(User.profile))
        .filter(User.id == current_user.id)
        .first()
    )

    if not user.profile:
        profile = Profile(user_id=user.id)
        db.add(profile)
        db.commit()

        # re-fetch again after insert
        user = (
            db.query(User)
            .options(joinedload(User.profile))
            .filter(User.id == user.id)
            .first()
        )

    return user




# update profile
@router.patch("/update_profile")
def update_profile(
    data: UpdateProfile,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    profile = db.query(Profile).filter(
        Profile.user_id == current_user.id
    ).first()

    if profile:
        # Update existing profile
        profile.full_name = data.full_name
        profile.phone_number = data.phone_number
        profile.address = data.address
        profile.profile_image = data.profile_image
    else:
        # Create new profile
        profile = Profile(
            user_id=current_user.id,
            full_name=data.full_name,
            phone_number=data.phone_number,
            address=data.address,
            profile_image=data.profile_image
        )
        db.add(profile)

    db.commit()
    db.refresh(profile)

    return {"message": "Profile updated successfully"}


# change password
@router.patch("/password_change")
def password_change(data:ChangePassword,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):

    # 1. Verify old password
    if not verify_password(
        data.old_password,
        current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Old password is incorrect")
    
    # update password

    current_user.hashed_password=hash_password(data.new_password)
    
    db.commit()

    return {
        "message":"password changed successfully"
    }
