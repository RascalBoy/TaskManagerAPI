from fastapi import APIRouter


from src.api.pages import router as pages_router
from src.api.users import router as users_router
from src.api.setup import router as setup_router
from src.api.projects import router as projects_router
from src.api.auth import router as auth_router
from src.api.tasks import router as tasks_router
from src.api.comments import router as comments_router

main_router = APIRouter()

main_router.include_router(pages_router)
main_router.include_router(setup_router)
main_router.include_router(auth_router)
main_router.include_router(users_router)
main_router.include_router(projects_router)
main_router.include_router(tasks_router)
main_router.include_router(comments_router)
