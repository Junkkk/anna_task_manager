import enum
from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Status(str, enum.Enum):
    NEW = 'New'
    PLANNED = 'Planned'
    IN_WORK = 'In work'
    COMPLETED = 'Completed'


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    description = Column(String)
    date = Column(DateTime)
    status = Column(Enum(Status))
    end_date = Column(DateTime, default=None)
    user = Column(Integer, ForeignKey("users.id"))
    user_id = relationship("User")
