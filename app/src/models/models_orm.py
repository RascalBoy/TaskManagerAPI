import enum

from src.database import session_factory, Base,str_20,str_50,str_200,intpk
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional
import datetime

class Complition_state(enum.Enum):
    started = 'Создана'
    in_progress = 'На выполнении'
    completed = 'Выполнена'


class Users_orm(Base):
    __tablename__ = 'users'
    id:Mapped[intpk] 
    login: Mapped[str_50]
    password: Mapped[str_200]
    nickname: Mapped[str_50]
    name: Mapped[str_50]
    second_name: Mapped[str_50]

class Projects_orm(Base):
    __tablename__ = 'projects'
    id:Mapped[intpk]
    title:Mapped[str_50]
    owner_id:Mapped[Optional[int|None]] = mapped_column(ForeignKey("users.id",ondelete="SET NULL"))

class Tasks_orm(Base):
    __tablename__ = 'tasks'
    id:Mapped[intpk] 
    title: Mapped[str_50]
    description: Mapped[str_200]
    complition_date: Mapped[datetime.datetime]
    complition_state: Mapped[Complition_state]
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id",ondelete="CASCADE"))
    tag_id:Mapped[Optional[int|None]] = mapped_column(ForeignKey("tags.id",ondelete="SET NULL"))

class Comments_orm(Base):
    __tablename__ = 'сomments'
    id:Mapped[intpk]
    title:Mapped[str_20]
    description:Mapped[str_200]
    user_id:Mapped[Optional[int|None]] = mapped_column(ForeignKey("users.id",ondelete="SET NULL"))
    project_id:Mapped[Optional[int|None]] = mapped_column(ForeignKey("projects.id",ondelete="SET NULL"))

class Tags_orm(Base):
    __tablename__ = 'tags'
    id:Mapped[intpk]
    title:Mapped[str_20]