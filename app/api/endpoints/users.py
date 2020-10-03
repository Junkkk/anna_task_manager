from fastapi import APIRouter, Depends
from typing import List
from app.api.utils.db import get_db
from app.user.schemas import User
from app.user.service import create_user, list_users
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/user", response_model=User)
async def create_category(item: User, db: Session = Depends(get_db)):
    return create_user(db=db, item=item)


@router.get("/user/list", response_model=List[User])
async def create_category(db: Session = Depends(get_db)):
    return list_users(db=db)
