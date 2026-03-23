from src.database import session_factory
from sqlalchemy import select,delete
from src.models.models_orm import Users_orm, Tasks_orm, Complition_state
from src.schemas.tasks import STaskCreate 
from src.schemas.other import PaginationDep

async def get_tasks(pagination:PaginationDep):
    async with session_factory() as session:
        query = (
            select(Tasks_orm)
            .limit(pagination.limit)
            .offset((pagination.page+1 * pagination.limit) - pagination.limit)
        )
        res = await session.execute(query)
        return res.scalars().all()
    
async def create_task(task:STaskCreate):
    async with session_factory() as session:
        try:
            new_task = Tasks_orm(
            title=task.title,
            description=task.description,
            completion_date=task.completion_date,
            completion_state=task.completion_state,
            project_id=task.project_id
            )
            session.add(new_task)
            await session.commit()
            return "Задача создана"
        except Exception as _ex:
            return _ex
    
async def change_task_status(task_id:int,new_state:Complition_state):
    async with session_factory() as session:
        task = await session.get(Tasks_orm,task_id)
        if not task:
            return "Такой задачи нет"
        
        task.completion_state = new_state
        await session.commit()
        return f"Статус задачи изменен на {new_state}"