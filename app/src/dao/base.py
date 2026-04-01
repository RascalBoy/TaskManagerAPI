from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parents[1]  
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi import HTTPException
from sqlalchemy import delete, select
from database import Base, session_factory
from src.dto.other import PaginationDep





class BaseDAO():
    model = None

    @classmethod
    async def find_one_or_none_by_id(cls, model_id, options=None):
        async with session_factory() as session:
            query = (
                select(cls.model).filter_by(id=model_id).options(*options) # type: ignore
            )
            res = await session.execute(query)
            return res.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, options=None, **filter_by):
        async with session_factory() as session:
            query = (
                select(cls.model).filter_by(**filter_by).options(*options) # type: ignore
            )
            res = await session.execute(query)
            return res.scalar_one_or_none()
        
    @classmethod
    async def find_all(cls, pagination:PaginationDep, options=None, **filter_by):
        async with session_factory() as session:
            query = (
                select(cls.model)# type: ignore
                .filter_by(**filter_by)
                .limit(limit=pagination.limit)
                .offset(offset = (pagination.page+1)*pagination.limit - pagination.limit)
                .options(*options) # type: ignore
            )
            res = await session.execute(query)
            return res.scalars().all()
        
    @classmethod
    async def delete_by_id(cls, model_id):
        async with session_factory() as session:
            user = session.get(cls.model, model_id)# type: ignore
            if not user:
                raise HTTPException(status_code=404)
            await session.delete(user)
            await session.commit()
