from pydantic import BaseModel, EmailStr
from typing import Optional


# ===============================
# USER SCHEMAS
# ===============================

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True  # Pydantic v2 way


# ===============================
# AUTH SCHEMAS
# ===============================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class TokenRefreshRequest(BaseModel):
    refresh_token: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None


# ========== PROJECT SCHEMAS ==========

class ProjectCreate(BaseModel):
    name: str
    cloud_provider: str
    repo_url: Optional[str] = None
    tf_path: Optional[str] = None


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    cloud_provider: Optional[str] = None
    repo_url: Optional[str] = None
    tf_path: Optional[str] = None


class ProjectRead(BaseModel):
    id: int
    name: str
    cloud_provider: str
    repo_url: Optional[str] = None
    tf_path: Optional[str] = None

    class Config:
        from_attributes = True
