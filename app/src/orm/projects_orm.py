from src.dto.projects import ProjectCreateDTO, ProjectRelDTO
from src.database import session_factory
from src.models.models_orm import Projects_orm, User_Projects_orm, Users_orm
from src.dto.other import PaginationDep

from sqlalchemy import delete, select, and_
from sqlalchemy.orm import selectinload

"""Получение списка проектов
Выдает список существующих проектов из бд
Диапазон регулируются через параметры Limit и page
"""
async def get_projects(pagination:PaginationDep):
    async with session_factory() as session:
        query = (
            select(Projects_orm)
            .limit(pagination.limit)
            .offset((pagination.page + 1) * pagination.limit
                    - pagination.limit)
            .options(selectinload(Projects_orm.tasks))
            
        )
        res = await session.execute(query)
        res_orm = res.scalars().all()
        result = [ProjectRelDTO.model_validate(row,from_attributes=True) for row in res_orm]
        return result
    

"""Создание проекта
Получает данные для создания проекта
Проверяет наличие пользователя в системе
Добавляет новый проект в бд
Добавляет запись об участнике проекта
"""
async def create_project(project:ProjectCreateDTO):
    async with session_factory() as session:

        user = await session.get(Users_orm,project.owner_id)
        if user is None:
            return "Такого пльзователя не существует"
        
        new_project = Projects_orm(
            title = project.title,
            owner_id=project.owner_id
        )
        session.add(new_project)

        await session.flush()

        query = (
            select(User_Projects_orm)
            .filter(and_(User_Projects_orm.user_id==project.owner_id,
                         User_Projects_orm.project_id==new_project.id))
        )
        res = await session.execute(query)
        if res.scalar_one_or_none() is not None:
            return {"data":"Такой пользователь уже прикреплен к такому проекту"}
        
        session.add(User_Projects_orm(
            user_id = new_project.owner_id,
            project_id = new_project.id
        ))
        await session.commit()
        return project


async def drop_project(project_id:int, owner_id:int):
    async with session_factory() as session:
        project = await session.get(Projects_orm,project_id)
        if not project:
            return "Проекта с таким id не существует"
        if project.owner_id != owner_id:
            return "Id Владельца проекта не совпадает с фактическим владельцем"
        # stmt = (
        #     delete(Projects_orm)
        #     .filter_by(id=project_id,owner_id=owner_id)
        # )
        await session.delete(project)
        await session.commit()
        return "Проект успешно удален"

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
            .filter(and_(User_Projects_orm.user_id==user_id,User_Projects_orm.project_id==project_id))
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