from fastapi import APIRouter
from src.orm import create_tables
import asyncio
router = APIRouter()

@router.get('/setup')
async def setup_database():
    await create_tables()
    return {'data':"Completed"}

    
