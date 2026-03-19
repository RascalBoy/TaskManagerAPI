from src.database import session_factory,Base,engine
from src.models.models_orm import Users_orm 
from src.schemas.users import SUserCreate 

def create_tables():
    Base.metadata.create_all(engine)

def create_user(user:SUserCreate):
    with session_factory() as session:
        session.add(Users_orm(
            login=user.login, 
            password=str(hash(user.password)),
            nickname=user.nickname,
            name=user.name,
            second_name=user.second_name
            ))
        session.commit()

def get_users():...

def get_tasks():...