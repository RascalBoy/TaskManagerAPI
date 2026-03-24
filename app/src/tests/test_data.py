from src.dto.users import UserCreateDTO
from src.dto.projects import ProjectCreateDTO
from src.dto.tasks import TaskCreateDTO
from src.orm.users_orm import create_user
from src.orm.projects_orm import create_project
from src.orm.tasks_orm import create_task

users = [{"login":"Test1",
          "password":"12345",
          "nickname":"RSB",
          "name":"Сергей",
          "second_name":"Марюнин"},
          {"login":"User1234",
          "password":"123456",
          "nickname":"Testoviy",
          "name":"МИХАИЛ",
          "second_name":"ГАВРИЛОВ"},
          {"login":"Gamer",
          "password":"1234321",
          "nickname":"Nick1234",
          "name":"Sergey",
          "second_name":"Marunin"},
          {"login":"Coper",
          "password":"1234Bazzo",
          "nickname":"BanzLove",
          "name":"Никита",
          "second_name":"Джигур"}]

projects = [
    {
        "title":"Тестовый проект 1",
        "owner_id": 1
    },
    {
        "title":"Лучший проект",
        "owner_id":3
    },
    {
        "title":"Культовый мультПроект",
        "owner_id":2
    },
    {
        "title":"PythonDevDiary",
        "owner_id":4
    },
]

tasks=[
    {
        "title": "Сварить пельмени",
        "description": "Необходисо сварить пельмени",
        "completion_state": "Создана",
        "project_id": 1,
    },
    {
        "title": "Задача сделать нормальный API",
        "description": "Очень хочется",
        "completion_state": "На выполнении",
        "project_id": 2,
    },
    {
        "title": "Тестовые данные",
        "description": "Создать тестовые данные для реализации тестов",
        "completion_state": "Выполнена",
        "project_id": 3,
    },
]

async def insert_test_data():
    _users = [UserCreateDTO(**u) for u in users]
    _projects = [ProjectCreateDTO(**p) for p in projects]
    _tasks = [TaskCreateDTO(**t) for t in tasks]
    for u in _users:
        await create_user(u)
    
    for p in _projects:
        await create_project(p)

    for t in _tasks:
        await create_task(t)