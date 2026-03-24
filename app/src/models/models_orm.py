from src.database import session_factory, Base,str_20,str_50,str_200,intpk

import enum
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey,text
from typing import Optional,Annotated
import datetime

class Complition_state(enum.Enum):
    started = 'Создана'
    in_progress = 'На выполнении'
    completed = 'Выполнена'


class Users_orm(Base):
    __tablename__ = 'users'
    id:Mapped[intpk] 
    login: Mapped[str_50] = mapped_column(unique=True)
    password: Mapped[str_200]
    nickname: Mapped[str_50]
    name: Mapped[str_50]
    second_name: Mapped[str_50]

    projects:Mapped[list["Projects_orm"]] = relationship()

class Projects_orm(Base):
    __tablename__ = 'projects'
    id:Mapped[intpk]
    title:Mapped[str_50]
    owner_id:Mapped[Optional[int|None]] = mapped_column(ForeignKey("users.id",ondelete="SET NULL"))

    tasks:Mapped[list["Tasks_orm"]] = relationship()

class User_Projects_orm(Base):
    __tablename__ = 'users_projects'
    id:Mapped[intpk]
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id",ondelete="CASCADE"))
    project_id:Mapped[int] = mapped_column(ForeignKey("projects.id",ondelete="CASCADE"))

class Tasks_orm(Base):
    __tablename__ = 'tasks'
    id:Mapped[intpk] 
    title: Mapped[str_50]
    description: Mapped[str_200]
    completion_state: Mapped[Complition_state]
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id",ondelete="CASCADE"))
    created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc',now())"))]
    updated_at = Annotated[datetime.datetime, 
                       mapped_column(server_default=text("TIMEZONE('utc',now())"),
                                    onupdate=datetime.datetime.now(datetime.timezone.utc))]

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