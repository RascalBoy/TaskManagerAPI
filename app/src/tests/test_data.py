from src.schemas.users import SUserCreate
from src.schemas.projects import SProjectCreate
from src.orm.users_orm import create_user
from src.orm.projects_orm import create_project

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

async def insert_test_data():
    _users = [SUserCreate(**u) for u in users]
    print(_users)
    _projects = [SProjectCreate(**p) for p in projects]
    print(_projects)
    for u in _users:
        await create_user(u)
    
    for p in _projects:
        await create_project(p)