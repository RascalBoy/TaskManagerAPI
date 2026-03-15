from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,AsyncSession
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import URL,create_engine,text
from config import settings

engine = create_engine(
    url= settings.DATABASE_URL_psycopq,
    echo=True,
    pool_size=5,
    max_overflow=10
)

with engine.connect() as q:
    res = q.execute(text("SELECT VERSION()"))
    print(f"{res}")