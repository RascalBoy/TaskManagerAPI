from fastapi import APIRouter
from src.orm import create_tables

router = APIRouter()

@router.get('/setup')
async def setup_database():
    try:
        create_tables()
        return {'data':'Completed'}
    except Exception as e:
        return e
    
