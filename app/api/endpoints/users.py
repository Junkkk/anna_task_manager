from fastapi import APIRouter, Depends, HTTPException
from app.api.utils.db import get_db
from app.user.schemas import User, UserCreate
from app.user.models import User as DBUser
from app.user.service import crud_user
from sqlalchemy.orm import Session
from app.api.utils.security import get_current_user


router = APIRouter()


@router.post("/", response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate
):
    """
    Create new user.
    """
    user = crud_user.get_by_name(db, name=user_in.name)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud_user.create(db, obj_in=user_in)
    return user


@router.get("/me", response_model=User)
def read_user_me(
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user),
):
    """
    Get current user.
    """
    return current_user


@router.get("/{user_id}", response_model=User)
def read_user_by_id(
    user_id: int,
    current_user: DBUser = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get a specific user by id.
    """
    user = crud_user.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud_user.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user
