from src.dto.projects import ProjectCreateDTO, ProjectRelDTO
from src.database import session_factory
from src.models.models_orm import Projects_orm, User_Projects_orm, Users_orm,Tasks_orm
from src.dto.other import PaginationDep

from sqlalchemy import delete, select, and_
from sqlalchemy.orm import selectinload

"""Получение списка проектов
Выдает список существующих проектов из бд
Диапазон регулируются через параметры Limit и page
"""

async def add_user(user_id:int, project_id:int):
    async with session_factory() as session:
        query = (
            select(User_Projects_orm)
            .filter(and_(User_Projects_orm.user_id==user_id,
                         User_Projects_orm.project_id==project_id))
        )
        res = await session.execute(query)
        if res.scalar_one_or_none() is not None:
            return {"data":"Такой пользователь уже прикреплен к такому проекту"}
        
        session.add(User_Projects_orm(
            user_id = user_id,
            project_id = project_id
        ))
        await session.commit()
        return "Пользователь успешно прикреплен к проекту"

async def remove_user(user_id:int, project_id:int):
    async with session_factory() as session:
        query = (
            select(User_Projects_orm)
            .filter(and_(User_Projects_orm.user_id==user_id,
                         User_Projects_orm.project_id==project_id))
        )
        res = await session.execute(query)
        if res.scalar_one_or_none() is None:
            return "Пользователь не прекреплен к проекту"
        stmt = (
            delete(User_Projects_orm)
            .filter_by(user_id=user_id,project_id=project_id)
        )
        await session.execute(stmt)
        await session.commit()
        return "Пользователь откреплен от проекта"