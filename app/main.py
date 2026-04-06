from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import auth, user, admin,transaction,summary
import app.models

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Data Processing & Access Control Backend",
    description=" FastAPI-based backend system implementing secure authentication (JWT & OTP), role-based access control (RBAC), and financial data processing with protected APIs for Admin and User roles",
    version="1.0.0")


# ---- CORS CONFIG ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)




# include routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(admin.router)
app.include_router(summary.router)
app.include_router(transaction.router)