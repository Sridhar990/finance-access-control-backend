from fastapi import HTTPException,status,APIRouter,Depends
from app.models.OTPEmail import OTPEmail
from app.models.user import User
from app.utils.otp import generate_otp
from app.core.security import hash_password,verify_password,create_access_token
from app.schemas.auth import UserRegister,OTPVerify,UserLogin,ForgotPassword,ResetPassword
from sqlalchemy.orm import Session 
from app.database import get_db
from datetime import datetime
from app.utils.email import send_otp_to_email
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/register",status_code=status.HTTP_201_CREATED)
def user_register(data:UserRegister,db:Session=Depends(get_db)):
    email = data.email.strip().lower()
    username=data.username.strip().lower()

    existing_user=db.query(User).filter((User.email==email)|(User.username==username)).first()

    # checking examil exist and user_is_active

    if existing_user:
        if existing_user.email==email:
            if existing_user.is_active:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email Already Registered Please login")
            

            #genearting otp for user is not active Is_active=False

            else:
                db.query(OTPEmail).filter(OTPEmail.user_id==existing_user.id).delete()
                db.commit()
                
                to_otp=generate_otp()


                otp=OTPEmail(user_id=existing_user.id,otp_code=to_otp,otp_expires_time=OTPEmail.generate_otp_expiry())

                db.add(otp)
                db.commit()

                send_otp_to_email(existing_user.email,to_otp)
                return{
                    "message":"otp resent. please verify you email."}
            
            # username already used 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="This username is already in use.Try a different one.")
    
    
    # if new user not exited with email and username and is_active =fasle then new user will be created

    new_user=User(username=username,email=email,hashed_password=hash_password(data.password),role="USER",is_active=False)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    to_otp=generate_otp()

    otp=OTPEmail(user_id=new_user.id,otp_code=to_otp,otp_expires_time=OTPEmail.generate_otp_expiry())
    db.add(otp)
    db.commit()

    send_otp_to_email(new_user.email,to_otp)
    return {
        "message":"registeration successfully. otp send to mail.please verify "
    }








# verify registeration and otp

@router.post("/verify-email")
def verify_email(data:OTPVerify,db:Session=Depends(get_db)):
    email = data.email.strip().lower()

    user=db.query(User).filter(User.email==email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")

    if user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="user already verified")
    #finding opt

    otp=db.query(OTPEmail).filter(OTPEmail.user_id==user.id).first()

    if not otp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="otp not found. please request new one")

    # checking otp expires
    if otp.otp_expires_time < datetime.utcnow():
        db.delete(otp)
        db.commit()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="otp expired, please request a new one")

    if data.otp!=otp.otp_code:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="invalid otp ")
    user.is_active=True
    db.delete(otp)
    db.commit()

    return {"message": "Email verified successfully. You can now login."}



# login route

@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm=Depends(),
    db: Session = Depends(get_db)):
    email = form_data.username.strip().lower()
    password=form_data.password

    user = db.query(User).filter(User.email ==email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    if not verify_password(password,user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalidd email or password")
    

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="user not verified please verify it")
    

    
    access_token=create_access_token(data={"sub":str(user.id)})

    return {
       "access_token":access_token,
       "token_type":"bearer" 
    }



# forgot password
@router.post("/forgot-password")
def forgotpassword(data:ForgotPassword,db:Session=Depends(get_db)):
     email = data.email.strip().lower()

     user=db.query(User).filter(User.email==email).first()

     if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
     
     if not user.is_active:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Email not verified")
     

     # delete old otp
     db.query(OTPEmail).filter(OTPEmail.user_id==user.id).delete()

     to_otp=generate_otp()

     otp=OTPEmail(user_id=user.id,otp_code=to_otp,otp_expires_time=OTPEmail.generate_otp_expiry())
     db.add(otp)
     db.commit()


     send_otp_to_email(user.email,to_otp)

     return {
         "message":"OTP send to email for password reset"
     }




@router.post("/reset-password")
def reset_password(
    data: ResetPassword,
    db: Session = Depends(get_db)):
    email = data.email.strip().lower()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    otp = db.query(OTPEmail).filter(
        OTPEmail.user_id == user.id
    ).first()

    if not otp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP not found"
        )

    if otp.otp_expires_time < datetime.utcnow():
        db.delete(otp)
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP expired"
        )

    if otp.otp_code != data.otp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid OTP"
        )

    
    user.hashed_password = hash_password(data.new_password)

    db.delete(otp)
    db.commit()

    return {
        "message": "Password reset successful. You can now login."
    }











                 





    


















