from sqlalchemy.orm import Session
from app.task import schemas, models


def create_task(db: Session, item: schemas.Task, user_id: int):
    db_item = models.Task(**item.dict())
    db_item.user = user_id
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def list_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter_by(user=user_id).all()
