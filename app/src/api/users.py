from fastapi import APIRouter, Form
from src.orm import create_user, get_user_by_id,get_users
from src.schemas.users import SUserRead,SUserCreate
from typing import List,Annotated
import asyncio

router = APIRouter()


@router.get("/users",response_model=list[SUserRead])
async def show_users():
    users = await get_users()
    return users

@router.get("/users/{user_id}",response_model=SUserRead)
async def show_user_by_id(user_id:int):
    user = await get_user_by_id(user_id)
    return user

@router.post("/users")
async def add_user(user:SUserCreate):
    await create_user(user)