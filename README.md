![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi)
![Database](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql)
![Deployment](https://img.shields.io/badge/Deployment-AWS%20EC2-FF9900?logo=amazonaws)
![Auth](https://img.shields.io/badge/Auth-JWT%20%2B%20RBAC-purple)




#  Finance Data Processing & Access Control Backend
---

### 📌 Overview
---
This project is a backend system built using FastAPI that provides secure authentication and role-based access control for financial data processing.

It simulates a real-world system where users (Admin/User) have controlled access to financial operations such as transactions and summaries.




### 🚀 Core Features
---
#### 🔑 Authentication

* User Registration with Email OTP verification

* Secure Login with JWT (Access Token)

* Password Hashing using Passlib (bcrypt)

* Token validation & protected routes

* Financial Transaction Management

* Financial Summary APIs

#### 👥 Authorization (RBAC)

* Role-based access (Admin / User)

* Route-level permission enforcement

* Secure dependency-based authorization

#### 🔐 Account Management

* View personal financial data

* Perform transactions

* Password Reset Flow

* Password Change

* Profile Management

#### 🛠 Admin Capabilities

* Admin User Management

* Access all financial data

* View system-wide summaries

* Role assignment control


### 🔐 Security Practices Implemented
---
* Password hashing with bcrypt

* JWT expiration handling

* Environment-based secrets management

* Route-level access control

* Separation of auth logic and business logic

#### 🛠 Tech Stack
---
* FastAPI – High-performance API framework

* SQLAlchemy – ORM for database interaction

* MySQL – Relational database

* python-jose – JWT handling

* Passlib (bcrypt) – Secure password hashing


### 📂 Project Structure
---
```
finance-access-control-backned/

├── app/

│   ├── core/   # Security, JWT, config

│   ├── models/        # SQLAlchemy models

│   ├── routes/        # API endpoints

│   ├── schemas/       # Pydantic request/response models

│   ├── utils/         # Utility functions

│   ├── database.py    # DB connection setup

│   └── main.py        # FastAPI app entry point

├── requirements.txt

├── .env.example

└── .gitignore
```

## ⚙️ Environment Configuration
---
The application uses environment variables for secure configuration.

* Create a .env file based on .env.example.

Example:
```
# Database Configuration
DB_USER=your_database_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_DATABASE_NAME=your_database_name

# JWT Configuration
SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Email (OTP)
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
```

Sensitive credentials are never stored in the repository.

### ▶️ Local Development Setup
---
## 1️⃣ Create Virtual Environment
```
python -m venv venv
```


* Activate it:

->Windows:
```
venv\Scripts\activate

```
->Linux / macOS:
```
source venv/bin/activate
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Configure Environment
```
cp .env.example .env
```

Update the variables accordingly.

### 4️⃣ Run Development Server
```uvicorn app.main:app --reload```


##### Server will run at:

```
http://127.0.0.1:8000
```

##### Swagger docs available at:
```
http://127.0.0.1:8000/docs
```
### 📬 API Endpoints

## 🔐Authentication

* POST /auth/register
* POST /auth/verify-email
* POST /auth/login
* POST /auth/forgot-password
* POST /auth/reset-password

## 👤 User APIs

* GET /users/me
* PATCH /users/update_profile
* PATCH /users/password_change

## 🛡️Admin APIs
* GET /admin/users
* PATCH /admin/users/{user_id}/disable
* PATCH /admin/users/{user_id}/enable
* DELETE /admin/users/{user_id}

## 💰 Financial Summary
* GET /summary/income
* GET /summary/expense
* GET /summary/balance

## 💳 Transactions

* GET /transactions/
* POST /transactions/
* DELETE /transactions/{tx_id}

### 📌 Submission Note

I attempted to submit this assignment via the provided portal before the deadline.

Due to technical issues with the platform/email domain, I am sharing my complete solution via this repository.

## Reference ID: TEBYL6XD
