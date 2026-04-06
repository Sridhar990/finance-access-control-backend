from pydantic import BaseModel
from typing import Optional,Literal
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: float
    type: Literal["income", "expense"]
    category: str
    description: Optional[str] = None

class TransactionOut(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    description: Optional[str]
    date: datetime

    class Config:
        orm_mode = True