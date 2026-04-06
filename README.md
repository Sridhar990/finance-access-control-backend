![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi)
![Database](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql)
![Deployment](https://img.shields.io/badge/Deployment-AWS%20EC2-FF9900?logo=amazonaws)
![Auth](https://img.shields.io/badge/Auth-JWT%20%2B%20RBAC-purple)




## 🔐 FastAPI RBAC Authentication System (Backend API)
---

### 📌 Overview
---
Production-ready FastAPI backend implementing a secure Role-Based Access Control (RBAC) authentication system.

This API supports JWT-based authentication, email OTP verification, role-based authorization, and is deployed on AWS EC2 using Gunicorn and Nginx with HTTPS.

The project demonstrates:

* Secure authentication flows

* Separation of concerns (modular architecture)

* Environment-based configuration

* Production deployment setup



### 🚀 Core Features
---
#### 🔑 Authentication

* User Registration with Email OTP verification

* Secure Login with JWT (Access Token)

* Password Hashing using Passlib (bcrypt)

* Token validation & protected routes

#### 👥 Authorization (RBAC)

* Role-based access (Admin / User)

* Route-level permission enforcement

* Secure dependency-based authorization

#### 🔐 Account Management

* Password Reset Flow

* Password Change

* Profile Management

#### 🛠 Admin Capabilities

* Admin User Management

* Admin Job Management

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

* Gunicorn – Production ASGI server

* Nginx – Reverse proxy

* AWS EC2 – Cloud deployment

### 📂 Project Structure
---
```
fastapi-rbac-auth-api/

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
### 🚀 Production Deployment
---
This backend is deployed on AWS EC2 with the following setup:

* Gunicorn (ASGI server)

* Nginx (reverse proxy)

* HTTPS (SSL certificate)

* systemd service for process management

* Production start command:

* gunicorn app.main:app -k uvicorn.workers.UvicornWorker


Nginx routes external HTTPS traffic to the internal Gunicorn server running on port 8000.


### 🔗 Related Repository
---
#### Frontend UI:
👉 [Sreamlit RBAC frontend](https://github.com/Sridhar990/rbac-auth-streamlit-ui)
