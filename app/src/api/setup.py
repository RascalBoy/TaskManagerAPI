from fastapi import APIRouter
from src.orm.setup_orm import create_tables
router = APIRouter()

@router.get('/setup')
async def setup_database():
    await create_tables()
    return {'data':"Completed"}

    
