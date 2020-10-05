from sqlalchemy.orm import Session
from app.task.schemas import TaskUpdate
from app.task import schemas, models
from fastapi.encoders import jsonable_encoder


def create_task(db: Session, item: schemas.Task, user_id: int):
    db_item = models.Task(**item.dict())
    db_item.user = user_id
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def list_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter_by(user=user_id).all()


def user_tasks_ids(db: Session, user_id: int):
    tasks_ids = []
    model_list = db.query(models.Task).filter_by(user=user_id).all()
    for model in model_list:
        tasks_ids.append(model.id)
    return tasks_ids


def task_update(db: Session, obj_in: TaskUpdate, task_id: int):
    db_obj = db.query(models.Task).get(task_id)
    in_obj = obj_in.dict(skip_defaults=True)
    for field in in_obj:
        setattr(db_obj, field, in_obj[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
