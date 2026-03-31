from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parents[1]  
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from sqlalchemy import delete, select
from database import Base, session_factory
from src.dto.other import PaginationDep





class BaseDAO():
    model = None

    @classmethod
    async def find_one_or_none_by_id(cls, model_id):
        async with session_factory() as session:
            query = (
                select(cls.model).filter_by(id=model_id) # type: ignore
            )
            res = await session.execute(query)
            return res.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with session_factory() as session:
            query = (
                select(cls.model).filter_by(**filter_by) # type: ignore
            )
            res = await session.execute(query)
            return res.scalar_one_or_none()
        
    @classmethod
    async def find_all(cls, pagination:PaginationDep, **filter_by):
        async with session_factory() as session:
            query = (
                select(cls.model)
                .filter_by(**filter_by)
                .limit(limit=pagination.limit)
                .offset(offset = (pagination.page+1)*pagination.limit - pagination.limit) # type: ignore
            )
            res = await session.execute(query)
            return res.scalars().all()
        
    @classmethod
    async def delete_by_id(cls, model_id):
        async with session_factory() as session:
            stmt = delete(cls.model).filter_by(id=model_id)
            await session.execute(stmt)
