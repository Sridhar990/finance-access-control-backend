from pydantic import BaseModel,EmailStr,Field

class UserRegister(BaseModel):
    email:EmailStr
    password:str=Field(... , min_length=8,max_length=67)
    username:str


class UserLogin(BaseModel):
    email:EmailStr
    password:str=Field(... , min_length=8,max_length=67)


class OTPVerify(BaseModel):
    email:EmailStr
    otp:str


class ForgotPassword(BaseModel):
    email:EmailStr


class ResetPassword(BaseModel):
    email:EmailStr
    otp:str
    new_password:str=Field(... , min_length=8,max_length=67)


# password change
class ChangePassword(BaseModel):
    old_password: str
    new_password: str



