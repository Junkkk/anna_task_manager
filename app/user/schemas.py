from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserBaseInDB(UserBase):
    name: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(UserBaseInDB):
    name: str
    password: str


class UserUpdate(UserBaseInDB):
    password: Optional[str] = None


class User(UserBaseInDB):
    pass


class UserInDB(UserBaseInDB):
    id: int
    hashed_password: str

