from src.schemas.projects import SProjectCreate
from src.database import session_factory,Base,engine
from sqlalchemy import select
from src.models.models_orm import Projects_orm

async def get_projects():
    async with session_factory() as session:
        query = select(Projects_orm)
        result = await session.execute(query)
        return result.scalars().all()

async def create_project(project:SProjectCreate):
    async with session_factory() as session:
        session.add(Projects_orm(
            title=project.title,
            owner_id=project.owner_id
        ))
        await session.commit()