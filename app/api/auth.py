from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app import models
from app.schemas import (
    UserCreate,
    UserRead,
    LoginRequest,
    TokenResponse,
    TokenRefreshRequest,
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"],
)


@router.post("/register", response_model=UserRead)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user account.
    """
    # Check if email already exists
    existing = (
        db.query(models.User)
        .filter(models.User.email == user_in.email)
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # Hash password
    hashed = hash_password(user_in.password)

    # Create user model
    user = models.User(
        email=user_in.email,
        name=user_in.name,
        password_hash=hashed,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    # FastAPI converts SQLAlchemy model -> UserRead
    return user


@router.post("/login", response_model=TokenResponse)
def login(login_in: LoginRequest, db: Session = Depends(get_db)):
    """
    Login with email + password.
    Returns access token + refresh token.
    """
    # Find user by email
    user = (
        db.query(models.User)
        .filter(models.User.email == login_in.email)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Check password
    if not verify_password(login_in.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Create tokens
    access_token = create_access_token({"sub": user.email})
    refresh_token = create_refresh_token({"sub": user.email})

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(body: TokenRefreshRequest):
    """
    Take a refresh token and return a new access + refresh token pair.
    """
    payload = decode_token(body.refresh_token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    email = payload.get("sub")
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    # Issue new pair of tokens
    new_access = create_access_token({"sub": email})
    new_refresh = create_refresh_token({"sub": email})

    return TokenResponse(
        access_token=new_access,
        refresh_token=new_refresh,
    )
