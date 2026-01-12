
# src/main.py
from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session
from datetime import timedelta

from core.config import settings
from src.db.connection import engine, get_db
from src.api import auth, todos
from src.models import *
from src.core.security import create_access_token
from src.schemas.user import UserCreate, AuthResponse, UserResponse, ErrorResponse
from src.services.user_service import UserService

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine, checkfirst=True)
    print("[OK] Database tables created")
    yield

app = FastAPI(
    title="Evolution of Todo API",
    description="Phase II Full-Stack Todo Web Application API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://todos-web-app-alpha.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        settings.frontend_url,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/test")
async def test_route():
    return {"message": "API test route is working"}

@app.post(
    "/api/v1/auth/signup-test",
    response_model=AuthResponse,
    responses={
        409: {"model": ErrorResponse, "description": "Email already registered"},
        422: {"model": ErrorResponse, "description": "Validation error"},
    },
    summary="[TEST] Register a new user",
    description="Create a new user account with email and password",
)
async def signup_test(
    response: Response,
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    if user_data.password != user_data.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"error": {"code": "VALIDATION_ERROR", "message": "Passwords do not match"}},
        )
    try:
        user = UserService.create_user(db, user_data.email, user_data.password)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"error": {"code": "VALIDATION_ERROR", "message": str(e)}},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    token = create_access_token(user.id, access_token_expires)
    return AuthResponse(
        user=UserResponse(
            id=user.id,
            email=user.email,
            createdAt=user.created_at,
            updatedAt=user.updated_at,
        ),
        session={"token": token, "expiresAt": user.created_at + access_token_expires},
    )

@app.get("/")
async def root():
    return {
        "name": "Evolution of Todo API",
        "version": "1.0.0",
        "docs": "/docs",
    }
