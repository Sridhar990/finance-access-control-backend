from sqlalchemy import Column,Integer,DateTime,ForeignKey,String
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class Profile(Base):
    __tablename__="profiles"

    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),unique=True,nullable=False)
    full_name=Column(String(100),nullable=True)
    phone_number=Column(String(20),unique=False,nullable=True)
    address=Column(String(300),nullable=True)
    profile_image=Column(String(255),nullable=True)

    updated_at=Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())

    user=relationship("User",back_populates="profile")
    


                   
