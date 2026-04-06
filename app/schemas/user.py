from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.schemas.profile import UpdateProfile


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime
    profile: UpdateProfile


    class Config:
        from_attributes = True

