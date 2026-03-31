from fastapi import APIRouter
from src.orm.setup_orm import create_tables,delete_tables
from src.tests.test_data import insert_test_data

router = APIRouter(tags=["Настройка БД"])

@router.get('/v1/setup')
async def setup_database()->dict[str,str]:
    await create_tables()

    return {'data':'Completed'}

'''Удалить эту функцию (Использовать только в разработке)'''
@router.get('/v1/drop')
async def drop_database()->dict[str,str]:
    await delete_tables()
    return {'data':'Completed'}

@router.get('/v1/test_data')
async def fill_database():
    await insert_test_data()
    return {'data':'Completed'}

@router.get('/reset')
async def reset_db():
    await delete_tables()
    await create_tables()
    await insert_test_data()
    return {'data':'Completed'}
