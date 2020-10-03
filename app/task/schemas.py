from pydantic import BaseModel
from datetime import datetime
from .models import Status


class Task(BaseModel):
    name: str
    description: str
    date: datetime
    status: Status = Status.NEW
    end_date: datetime = None

    class Config:
        orm_mode = True
