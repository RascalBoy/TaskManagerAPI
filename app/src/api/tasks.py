from fastapi import APIRouter, Depends,HTTPException
from src.orm.tasks_orm import delete_task, get_tasks, create_task, change_task_status
from src.dto.other import PaginationDep
from src.dto.tasks import TaskCreateDTO
from src.models.models_orm import Complition_state
from typing import Annotated

router = APIRouter()

TaskCreateDTODep = Annotated[TaskCreateDTO,Depends(TaskCreateDTO)]

@router.get("/v1/tasks", response_model=dict[str,list[TaskCreateDTO]])
async def show(pagination:PaginationDep):
    result = await get_tasks(pagination)
    return {"data":result}

@router.post("/v1/tasks")
async def add(task:TaskCreateDTODep):
    try:
        result = await create_task(task)
        return {"state":"success", 'data':result}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")
    
@router.patch("/v1/tasks")
async def change_status(id:int, state:Complition_state):
    try:
        result = await change_task_status(id,state)
        return  {"state":"success", 'data':result}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")
    
@router.delete("/v1/tasks")
async def delete(task_id:int,user_id:int):
    try:
        result = await delete_task(task_id,user_id)
        return {"state":"success", "data":result}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")

