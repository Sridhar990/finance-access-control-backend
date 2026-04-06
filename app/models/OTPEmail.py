from sqlalchemy import Integer,String,Column,DateTime,ForeignKey
from app.database import Base
from sqlalchemy.sql import func
from datetime import datetime,timedelta


class OTPEmail(Base):
    __tablename__="otp_To_Email"

    id=Column(Integer,primary_key=True,autoincrement=True)

    user_id=Column(Integer(),ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    otp_code=Column(String(6),nullable=False)
    
    otp_expires_time=Column(DateTime,nullable=False)

    created_at=Column(DateTime(timezone=True),server_default=func.now())

    @staticmethod
    def generate_otp_expiry(minutes:int=10):
        return datetime.utcnow() + timedelta(minutes=minutes)
    
