from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.transaction import Transaction
from app.core.deps import get_current_user

router = APIRouter(prefix="/summary", tags=["Summary"])

# total income
@router.get("/income")
def total_income(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    q = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "income")

    if current_user.role != "ADMIN":
        q = q.filter(Transaction.user_id == current_user.id)

    return {"total_income": q.scalar() or 0}


@router.get("/expense")
def total_expense(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    q = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "expense")

    if current_user.role != "ADMIN":
        q = q.filter(Transaction.user_id == current_user.id)

    return {"total_expense": q.scalar() or 0}


@router.get("/balance")
def balance(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    income = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "income")
    expense = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "expense")

    if current_user.role != "ADMIN":
        income = income.filter(Transaction.user_id == current_user.id)
        expense = expense.filter(Transaction.user_id == current_user.id)

    return {
        "balance": (income.scalar() or 0) - (expense.scalar() or 0)
    }