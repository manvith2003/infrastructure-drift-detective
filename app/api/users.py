from fastapi import APIRouter, Depends

from app.core.auth import get_current_user
from app.schemas import UserRead
from app import models

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],
)


@router.get("/me", response_model=UserRead)
def read_current_user(
    current_user: models.User = Depends(get_current_user),
):
    """
    Return the currently authenticated user.
    """
    return current_user
