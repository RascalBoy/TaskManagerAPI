from src.database import session_factory
from src.models.models_orm import Users_orm, Tasks_orm, Projects_orm, Complition_state
from src.dto.tasks import TaskCreateDTO 
from src.dto.other import PaginationDep

from sqlalchemy import and_, select,delete

async def get_tasks(pagination:PaginationDep):
    async with session_factory() as session:
        query = (
            select(Tasks_orm)
            .limit(pagination.limit)
            .offset((pagination.page+1 * pagination.limit) - pagination.limit)
        )
        res = await session.execute(query)
        return res.scalars().all()
    
async def create_task(task:TaskCreateDTO):
    async with session_factory() as session:
        try:
            new_task = Tasks_orm(
            title=task.title,
            description=task.description,
            completion_state=task.completion_state,
            project_id=task.project_id
            )
            session.add(new_task)
            await session.commit()
            return "Задача создана"
        except Exception as _ex:
            return "Что то пошло не так"
    
async def change_task_status(task_id:int,new_state:Complition_state):
    async with session_factory() as session:
        task = await session.get(Tasks_orm,task_id)
        if not task:
            return "Такой задачи нет"
        
        task.completion_state = new_state
        await session.commit()
        return f"Статус задачи изменен на {new_state}"

async def delete_task(task_id:int, user_id:int):
    async with session_factory() as session:
        task = await session.get(Tasks_orm,task_id)
        if task is None:
            return "Задачи не существует"
        project = await session.get(Projects_orm,task.project_id)
        if project.owner_id == user_id:
            await session.delete(task)
            await session.commit()
            return "Задача успешно удалена"
        else:
            return "Ошибка доступа"
