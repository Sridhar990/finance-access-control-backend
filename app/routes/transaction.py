from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.core.deps import get_current_user

router = APIRouter(prefix="/transactions", tags=["Transactions"])

# transaction created route
@router.post("/", response_model=TransactionOut)
def create_transaction(data: TransactionCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    tx = Transaction(
        user_id=current_user.id,
        amount=data.amount,
        type=data.type,
        category=data.category,
        description=data.description
    )
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx


# transtion Get Route
@router.get("/", response_model=List[TransactionOut])
def get_transactions(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if current_user.role == "ADMIN":
        return db.query(Transaction).all()

    return db.query(Transaction).filter(Transaction.user_id == current_user.id).all()



# Delete

@router.delete("/{tx_id}")
def delete_transaction(tx_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    tx = db.query(Transaction).filter(Transaction.id == tx_id).first()

    if not tx:
        raise HTTPException(status_code=404, detail="Not found")

    if current_user.role != "ADMIN" and tx.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(tx)
    db.commit()

    return {"msg": "Deleted"}
