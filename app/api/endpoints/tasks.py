from fastapi import APIRouter, Depends
from app.api.utils.db import get_db
from app.task.schemas import Task
from app.task.service import create_task, list_tasks
from sqlalchemy.orm import Session
from app.user.models import User as DBUser
from app.api.utils.security import get_current_user
from typing import List


router = APIRouter()


@router.post("/task", response_model=Task)
async def task_create(
        item: Task,
        current_user: DBUser = Depends(get_current_user),
        db: Session = Depends(get_db)):
    print('task_create', current_user)
    return create_task(db=db, item=item, user_id=current_user.id)


@router.get("/task", response_model=List[Task])
async def task_list(
        current_user: DBUser = Depends(get_current_user),
        db: Session = Depends(get_db)):
    print('endpoint ', current_user.id)

    return list_tasks(db=db, user_id=current_user.id)
