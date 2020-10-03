from sqlalchemy import Column, Integer, String, DateTime
from db.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)
