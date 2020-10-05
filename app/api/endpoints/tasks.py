from fastapi import APIRouter, Depends, HTTPException
from app.api.utils.db import get_db
from app.task.schemas import Task, TaskUpdate
from app.task.service import create_task, list_tasks, task_update, user_tasks_ids
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
    return create_task(db=db, item=item, user_id=current_user.id)


@router.get("/task/list", response_model=List[Task])
async def task_list(
        current_user: DBUser = Depends(get_current_user),
        db: Session = Depends(get_db)):

    return list_tasks(db=db, user_id=current_user.id)


@router.patch('/task/{task_id}', response_model=TaskUpdate)
async def update_task(
        task_id: int,
        item: TaskUpdate,
        # current_user: DBUser = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    # if task_id not in user_tasks_ids(db, current_user.id):
    #     raise HTTPException(
    #         status_code=403, detail="you do not have permission to edit"
    #     )
    return task_update(db=db, obj_in=item, task_id=task_id)
