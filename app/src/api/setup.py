from fastapi import APIRouter
from src.orm.setup_orm import create_tables,delete_tables
from src.tests.test_data import insert_test_data
from src.modules.response_creator import ResponseCreator

router = APIRouter(tags=["Настройка БД"])

@router.get('/v1/setup')
async def setup_database()->dict[str,str]:
    await create_tables()

    return ResponseCreator.create_response(message="Создание БД успешно выполнено")

'''Удалить эту функцию (Использовать только в разработке)'''
@router.get('/v1/drop')
async def drop_database()->dict[str,str]:
    await delete_tables()
    return ResponseCreator.create_response(message="Удаление БД успешно выполнено")

@router.get('/v1/test_data')
async def fill_database():
    await insert_test_data()
    return ResponseCreator.create_response(message="Тестовые данные успешно загружены")

@router.get('/reset')
async def reset_db():
    await delete_tables()
    await create_tables()
    await insert_test_data()
    return ResponseCreator.create_response(message="БД успешно восстановлена в v1 версию")
