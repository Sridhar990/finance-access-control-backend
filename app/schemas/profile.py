from pydantic import BaseModel
from typing import Optional

class UpdateProfile(BaseModel):
    full_name:Optional[str]=None
    phone_number:Optional[str]=None
    address:Optional[str]=None
    profile_image:Optional[str]=None
    
class Config:
        from_attributes = True