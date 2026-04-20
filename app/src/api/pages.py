from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from src.api.projects import show
from src.jwt.token_verifier import verify_token
router = APIRouter(prefix="/pages", tags=["Страницы"])

templates = Jinja2Templates(directory="src/templates")

@router.get("/projects",name="Получение проектов пользователем")
async def get_projects(request:Request, projects=Depends(show)):
    return templates.TemplateResponse(name="projects.html",context={"request":request, "projects":projects})