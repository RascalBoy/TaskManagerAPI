from src.dto.users import UserCreateDTO
from src.dto.projects import ProjectCreateDTO
from src.dto.tasks import TaskCreateDTO
from src.dto.comments import CommentsCreateDTO
from src.dao.users import Users
from src.orm.projects_orm import create_project
from src.orm.tasks_orm import create_task
from src.orm.comments_orm import create_comment
from src.database import session_factory 

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
        "title":"Кулинария для чайников",
        "owner_id": 1
    },
    {
        "title":"Разработка платформера",
        "owner_id":3
    },
    {
        "title":"Рисуем мультики",
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
        "project_id": 4,
    },
    {
        "title": "Сделать раскадровку для первой сцены",
        "description": "Нарисовать раскадровку к первой сцене мультфильма",
        "completion_state": "На выполнении",
        "project_id": 3,
    },
]
comments=[
    {
        "title":"Главное не забыть перец",
        "description":"Для вкусных пельменей нужно преобрести и использовать перец",
        "user_id":1,
        "task_id":1
    },
    {
        "title":"Нужно переделать бд",
        "description":"Вроде все неплохо но как проектировщик бд я все еще слабоват",
        "user_id":2,
        "task_id":3
    },
    {
        "title":"Главное не забыть перец",
        "description":"Для вкусных пельменей нужно преобрести и использовать перец",
        "user_id":1,
        "task_id":1
    },
    {
        "title":"Нужно переделать бд",
        "description":"Вроде все неплохо но как проектировщик бд я все еще слабоват",
        "user_id":2,
        "task_id":3
    },
    {
        "title":"Главное не забыть перец",
        "description":"Для вкусных пельменей нужно преобрести и использовать перец",
        "user_id":1,
        "task_id":1
    },
    {
        "title":"Нужно переделать бд",
        "description":"Вроде все неплохо но как проектировщик бд я все еще слабоват",
        "user_id":2,
        "task_id":3
    },
]

async def insert_test_data():
    _users = [UserCreateDTO(**u) for u in users]
    _projects = [ProjectCreateDTO(**p) for p in projects]
    _tasks = [TaskCreateDTO(**t) for t in tasks]
    _comments = [CommentsCreateDTO(**c) for c in comments]
    for u in _users:
        await Users.create(u)
    
    for p in _projects:
        await create_project(p)

    for t in _tasks:
        await create_task(t)

    for c in _comments:
        await create_comment(c)