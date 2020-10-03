from typing import List
from sqlalchemy.orm import Session
from app.user import schemas, models
from datetime import datetime


def create_user(db: Session, item: schemas.User):
    db_item = models.User(**item.dict())
    db_item.date = datetime.now()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def list_users(db: Session) -> List[schemas.User]:
    return db.query(models.User).all()
