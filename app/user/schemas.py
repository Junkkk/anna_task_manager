from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name: str
    password: str

    class Config:
        orm_mode = True
