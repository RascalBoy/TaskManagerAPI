from fastapi import APIRouter, Form
from src.orm import create_user
from src.schemas.users import SUserRead,SUserCreate
from typing import List,Annotated

router = APIRouter()

@router.get("/users/{user_id}")
async def show_user_by_id(user_id:int) -> int:
    return user_id

@router.get("/users")
async def show_users() ->List[SUserRead]:
    return []

@router.post("/users/add")
async def add_user(user:SUserCreate):
    create_user(user)