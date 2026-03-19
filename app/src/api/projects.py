from fastapi import APIRouter,HTTPException
from src.schemas.projects import SProjectCreate
from src.orm.projects_orm import get_projects, create_project

router = APIRouter()

@router.get("/projects", response_model=list[SProjectCreate])
async def show_projects():
    result = await get_projects()
    if not result:
        raise HTTPException(status_code=404,detail="Проектов в бд нет")
    
    return result

@router.post("/projects")
async def add_project(project:SProjectCreate):
    await create_project(project=project)

    
    