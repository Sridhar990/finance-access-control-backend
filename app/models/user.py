from sqlalchemy import Column,Integer,String,DateTime,Boolean
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(Base):
 __tablename__ = "users"

 id=Column(Integer,primary_key=True,autoincrement=True)
 username=Column(String(50),unique=True,nullable=False)
 email=Column(String(100),unique=True,nullable=False)
 hashed_password=Column(String(255),nullable=False)
 role=Column(String(20),nullable=False,default="USER")
 is_active=Column(Boolean,default=True)
 created_at=Column(DateTime(timezone=True),server_default=func.now())

 profile=relationship("Profile",back_populates="user",uselist=False,cascade="all, delete-orphan")