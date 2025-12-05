from datetime import datetime, timedelta

import bcrypt
from jose import JWTError, jwt

from app.config import settings


# ===============================
# PASSWORD HASHING FUNCTIONS
# ===============================

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    Returns a hash string that we can store in the database.
    """
    # bcrypt works with bytes, so encode the string
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    # store as string (decode back to utf-8)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password by comparing plain text with a hashed one.
    """
    plain_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_bytes, hashed_bytes)


# ===============================
# JWT TOKEN FUNCTIONS
# ===============================

def create_access_token(data: dict, expires_delta: int = 60 * 24):
    """
    Create a JWT token.
    expires_delta: minutes (default: 24 hours)
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt


def decode_token(token: str):
    """Decode a JWT token and return the payload dict, or None if invalid."""
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
        return payload
    except JWTError:
        return None

def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    """
    Create a refresh token (longer lifetime than access token).
    Default: 7 days.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=7))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt
