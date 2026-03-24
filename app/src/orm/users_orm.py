from src.models.models_orm import Users_orm
from src.dto.users import UserCreateDTO, UserRelDTO
from src.models.models_orm import Projects_orm
from src.dto.other import PaginationDep
from src.modules.hash_tools import hasher
from src.database import session_factory

from sqlalchemy.orm import selectinload
from sqlalchemy import select,delete

async def create_user(user:UserCreateDTO):
    async with session_factory() as session:
        session.add(Users_orm(
            login=user.login,
            password=str(hasher.to_md5(user.password)),
            nickname=user.nickname,
            name=user.name,
            second_name=user.second_name
            ))
        await session.commit()

async def get_user_by_id(user_id:int):
    async with session_factory() as session:
        query = (
            select(Users_orm)
            .filter_by(id = user_id)
            .options(selectinload(Users_orm.projects).selectinload(Projects_orm.tasks))
        )
        res = await session.execute(query)
        result_orm = res.scalars().one()
        result = UserRelDTO.model_validate(result_orm, from_attributes=True)
        return result
    
async def get_users(pagination:PaginationDep):
    async with session_factory() as session:
        query = (
            select(Users_orm)
            .limit(limit=pagination.limit)
            .offset(offset=((pagination.page+1)*pagination.limit - pagination.limit))
            .options(selectinload(Users_orm.projects).selectinload(Projects_orm.comments),
                     selectinload(Users_orm.projects).selectinload(Projects_orm.tasks))
        )
        res = await session.execute(query)
        res_orm = res.scalars().all()
        result = [UserRelDTO.model_validate(row,from_attributes=True) for row in res_orm]
        return result
    
async def delete_user(user_id:int):
    async with session_factory() as session:
        stmt = (delete(Users_orm)
        .filter_by(id=user_id))
        await session.execute(stmt)
        await session.commit()

async def change_user_password(user_id:int, password:str)->str|None:
    async with session_factory() as session:
        user = await session.get(Users_orm,user_id)
        if not user:
            return "Пользователя с таким id не существует"
        
        user.password = str(hasher.to_md5(password))
        await session.commit()
        return "Пароль изменен"
    
async def auth_user(login:str, user_password:str):
    async with session_factory() as session:
       query = (
           select(Users_orm)
           .filter_by(login=login, password=str(hasher.to_md5(user_password)))
       )
       res = await session.execute(query)
       return res.scalars().one_or_none()

        
        

