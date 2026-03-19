from fastapi import APIRouter

from src.api.users import router as users_router
from src.api.setup import router as setup_router

main_router = APIRouter()

main_router.include_router(setup_router)
main_router.include_router(users_router)