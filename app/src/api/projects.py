from src.dto.projects import ProjectCreateDTO,ProjectRelDTO
from src.dto.other import PaginationDep
from src.orm.projects_orm import get_projects, create_project, add_user,remove_user,drop_project

from typing import Annotated
from fastapi import APIRouter,HTTPException,Depends

router = APIRouter(tags=["Проекты"])

SProjectCreateDep = Annotated[ProjectCreateDTO,Depends(ProjectCreateDTO)]

@router.get("/v1/projects")
async def show(pagination:PaginationDep):
    result = await get_projects(pagination)

    if not result:
        raise HTTPException(status_code=404,detail="Проектов в бд нет")
    
    return result

@router.post("/v1/projects")
async def add(project:ProjectCreateDTO):
    try:
        res = await create_project(project=project)
        return {"state":"success",
                "data":res}
    except Exception as _ex:
        raise HTTPException(status_code=500,detail=_ex)
    
@router.delete("/v1/projects")
async def remove(project_id:int, owner_id:int):
    try:
        res = await drop_project(project_id,owner_id)
        return {"state":"success",
                "data":f"{res}"}
    except Exception as _ex:
        raise HTTPException(status_code=500,detail=f"{_ex}")
    
@router.patch("/v1/projects/add_user")
async def add_user_to_project(user_id:int, project_id:int):
    try:
        res = await add_user(user_id,project_id)
        return {"status":"Completed", "data":res}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")
    
@router.patch("/v1/projects/remove_user")
async def remove_user_from_project(user_id:int, project_id:int):
    try:
        res = await remove_user(user_id,project_id)
        return {"status":"Completed", "data":res}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")



