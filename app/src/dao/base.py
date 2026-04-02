from pathlib import Path
import sys
from typing import Any
ROOT_DIR = Path(__file__).resolve().parents[1]  
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi import HTTPException
from sqlalchemy import delete, select, update
from sqlalchemy.orm import DeclarativeBase
from database import Base, session_factory
from src.dto.other import PaginationDep
from pydantic import BaseModel

class BaseDAO():
    model = None

    @classmethod
    async def find_one_or_none_by_id(cls, model_id, options=None):
        async with session_factory() as session:
            query = (
                select(cls.model).filter_by(id=model_id) # type: ignore
            )
            if options:
                query = query.options(*options)
            res = await session.execute(query)
            return res.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, options=None, **filter_by):
        async with session_factory() as session:
            query = (
                select(cls.model).filter_by(**filter_by) # type: ignore
            )
            if options:
                query = query.options(*options)
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
            )
            if options:
                query = query.options(*options)
            res = await session.execute(query)
            return res.scalars().all()
        
    @classmethod
    async def delete_by_id(cls, model_id):
        async with session_factory() as session:
            obj = await session.get(cls.model, model_id)# type: ignore
            if not obj:
                raise HTTPException(status_code=404)
            await session.delete(obj)
            await session.commit()
    
    @classmethod
    async def delete(cls, **filter_by):
        async with session_factory() as session:
            obj = await cls.find_one_or_none(**filter_by)
            if not obj:
                raise HTTPException(status_code=500,detail=f"Удаление не удалось")
            await session.delete(obj)
            await session.commit()

    @classmethod
    async def insert(cls, object):
        async with session_factory() as session:
            try:
                obj = cls.model(**object.model_dump()) # type: ignore
                session.add(obj)
                await session.commit()
            except Exception as ex:
                raise HTTPException(status_code=500,detail=f"Добавление не удалось - {ex}")
            
    @classmethod
    async def update_column_by_id(cls, column, value:Any,**filter_by):
        async with session_factory() as session:
            stmt = (
                update(cls.model) # type: ignore
                .filter_by(**filter_by)
                .values({column.key:value})
                .returning(cls.model) # type: ignore
            )
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one_or_none()