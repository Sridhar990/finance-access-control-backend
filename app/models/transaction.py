from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    amount = Column(Float, nullable=False)
    type = Column(String(20), nullable=False)  
    category = Column(String(50), nullable=False)
    description = Column(String(225))

    date = Column(DateTime, default=datetime.utcnow)
