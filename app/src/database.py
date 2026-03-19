from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,AsyncSession
from sqlalchemy.orm import Session,sessionmaker,DeclarativeBase,mapped_column
from sqlalchemy import URL,create_engine,text,String
from typing import Annotated
from src.config import settings

engine = create_engine(url=settings.DATABASE_URL_psycopq,echo=True)

session_factory = sessionmaker(engine)

str_20 = Annotated[str,String(20)]
str_50 = Annotated[str,String(50)]
str_200= Annotated[str,String(200)]
intpk = Annotated[int,mapped_column(primary_key=True)]

class Base(DeclarativeBase):
    type_annotation_map={
        str_20:String(20),
        str_50:String(50),
        str_200:String(200)
    }