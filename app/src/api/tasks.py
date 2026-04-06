from fastapi import APIRouter, Depends,HTTPException
from src.dto.other import PaginationDep
from src.dto.tasks import TaskCreateDTO,TaskRelDTO
from src.models.models_orm import Complition_state
from src.dao.tasks import Tasks
from typing import Annotated
from modules.response_creator import ResponseCreator
from sqlalchemy.orm import selectinload

router = APIRouter(tags=["Задачи"])

TaskCreateDTODep = Annotated[TaskCreateDTO,Depends(TaskCreateDTO)]

@router.get("/v1/tasks")
async def show(pagination:PaginationDep):
    result = await Tasks.find_all(pagination, options=[selectinload(Tasks.model.comments)])
    if not result:
        return ResponseCreator.create_response(status_code=404,message="Задач нет")
    return ResponseCreator.create_response(object=[TaskRelDTO.model_validate(row,) for row in result])

@router.post("/v1/tasks")
async def add(task:TaskCreateDTODep):
    try:
        result = await Tasks.insert(task)
        return ResponseCreator.create_response(message="Задача добавлена")
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")

@router.put("/v1/tasks")
async def edit(task:TaskCreateDTO,task_id:int):
    try:
        await Tasks.update(task, id=task_id)
        return ResponseCreator.create_response(message=f"Задача успешно изменена")
    except Exception as _ex:
        return ResponseCreator.create_response(500,"Error",message=f"{_ex}")


@router.patch("/v1/tasks")
async def change_status(id:int, state:Complition_state):
    try:
        result = await Tasks.update_column_by_id(Tasks.model.completion_state,state,id=id)
        return ResponseCreator.create_response(message=f"Задача изменила статус на {state}")
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")
    
@router.delete("/v1/tasks")
async def delete(task_id:int):
    try:
        result = await Tasks.delete(id=task_id)
        return ResponseCreator.create_response(message=f"Задача успешно удалена")
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")

