from fastapi import APIRouter, Depends
from app.api.utils.db import get_db
from app.task.schemas import Task
from app.task.service import create_task, list_tasks
from sqlalchemy.orm import Session
from app.user.schemas import User
from typing import List


router = APIRouter()


@router.post("/task/{user_id}", response_model=Task)
async def create_category(item: Task, user_id: int, db: Session = Depends(get_db)):
    return create_task(db=db, item=item, user_id=user_id)


@router.get("/task/list/{user_id}", response_model=List[Task])
async def task_list(user_id: int, db: Session = Depends(get_db)):
    return list_tasks(db=db, user_id=user_id)
