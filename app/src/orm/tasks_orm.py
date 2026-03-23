from src.database import session_factory
from sqlalchemy import select,delete
from src.models.models_orm import Users_orm, Tasks_orm
from src.schemas.tasks import STaskCreate 
from src.schemas.other import PaginationDep

async def get_tasks(pagination:PaginationDep):
    async with session_factory() as session:
        query = (
            select(Tasks_orm)
            .limit(pagination.limit)
            .offset(pagination.page * pagination.limit - pagination.limit)
        )
        res = await session.execute(query)
        return res.scalars().all()
    
async def create_task(task:STaskCreate):
    async with session_factory() as session:
        new_task = Tasks_orm(
        title=task.title,
        description=task.description,
        complition_date=task.completion_date,
        complition_state=task.completion_state,
        project_id=task.project_id,
        tag_id=task.tag_id
        )