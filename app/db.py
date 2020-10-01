import enum
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Enum, ForeignKey, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/task"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Status(enum.Enum):
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
    user_id = orm.relationship("User")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)