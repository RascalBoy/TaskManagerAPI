import logging
logger = logging.getLogger(__name__)

from sqlalchemy import and_, delete, select

from src.dto.projects import ProjectCreateDTO
from src.modules.hash_tools import get_hash
from src.models.models_orm import User_Projects_orm
from src.database import session_factory
from src.dao.base import BaseDAO

class User_Projects(BaseDAO):
    model = User_Projects_orm

    @classmethod
    async def add_user(cls,user_id:int, project_id:int):
        async with session_factory() as session:
            logger.error(project_id)
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

    @classmethod
    async def remove_user(cls,user_id:int, project_id:int):
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