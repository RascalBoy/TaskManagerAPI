from src.dao.users import Users
from src.models.models_orm import Projects_orm, Tasks_orm
from src.modules.response_creator import ResponseCreator
from src.dto.projects import ProjectCreateDTO,ProjectRelDTO
from src.dto.other import PaginationDep
from src.dao.projects import Projects
from src.orm.projects_orm import get_projects, create_project, add_user,remove_user,drop_project
from sqlalchemy.orm import selectinload
from typing import Annotated
from fastapi import APIRouter,HTTPException,Depends

router = APIRouter(tags=["Проекты"])

SProjectCreateDep = Annotated[ProjectCreateDTO,Depends(ProjectCreateDTO)]

@router.get("/v1/projects") #Done
async def show(pagination:PaginationDep):
    result = await Projects.find_all(pagination,options=[
        selectinload(Projects_orm.tasks)
        .selectinload(Tasks_orm.comments)])

    if not result:
        raise HTTPException(status_code=404,detail="Проектов в бд нет")
    
    return ResponseCreator.create_response(object=[
        ProjectRelDTO.model_validate(row, from_attributes=True) for row in result])

@router.post("/v1/projects") #Done
async def add(project:ProjectCreateDTO):
    try:
        user = await Users.find_one_or_none_by_id(project.owner_id)
        if not user:
            raise HTTPException(status_code=404,
                                detail="Пользователя для создания проекта не существует")
        res = await Projects.insert(project)
        return ResponseCreator.create_response(message="Проект успешно создан",object=project)
    except Exception as _ex:
        raise HTTPException(status_code=500,detail=f"{_ex}")
    
@router.delete("/v1/projects") #Done
async def remove(project_id:int, owner_id:int):
    try:
        res = await Projects.delete_by_id(project_id)
        return ResponseCreator.create_response(message="Проект успешно удален")
    except Exception as _ex:
        raise HTTPException(status_code=500,detail=f"{_ex}")
    
@router.patch("/v1/projects/add_user") #Not
async def add_user_to_project(user_id:int, project_id:int):
    try:
        res = await add_user(user_id,project_id)
        return {"status":"Completed", "data":res}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")
    
@router.patch("/v1/projects/remove_user") #Not
async def remove_user_from_project(user_id:int, project_id:int):
    try:
        res = await remove_user(user_id,project_id)
        return {"status":"Completed", "data":res}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")



