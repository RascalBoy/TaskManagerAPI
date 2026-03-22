from fastapi import APIRouter
from src.orm.setup_orm import create_tables,delete_tables
router = APIRouter()

@router.get('/setup')
async def setup_database()->dict[str,str]:
    await create_tables()
    return {'data':"Completed"}

'''Удалить эту функцию (Использовать только в разработке)'''
@router.get('/drop')
async def drop_database()->dict[str,str]:
    await delete_tables()
    return {'data':"Completed"}

    
