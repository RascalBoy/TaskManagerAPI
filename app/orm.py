from database import session_factory,Base,engine
from models_orm import Users_orm 
from models.user_models import MUserCreate 

def create_tables():
    Base.metadata.create_all(engine)

def create_user(user:MUserCreate):
    with session_factory() as session:
        session.add(Users_orm(
            login=user.login, 
            password=user.password,
            nickname=user.nickname,
            name=user.name,
            second_name=user.second_name
            ))
        session.commit()