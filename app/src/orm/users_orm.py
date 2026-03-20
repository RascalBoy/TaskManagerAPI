from src.database import session_factory,Base,engine
from sqlalchemy import select,delete
from src.models.models_orm import Users_orm
from src.schemas.users import SUserCreate 
from src.schemas.other import PaginationDep

async def create_user(user:SUserCreate):
    async with session_factory() as session:
        session.add(Users_orm(
            login=user.login, 
            password=str(hash(user.password)),
            nickname=user.nickname,
            name=user.name,
            second_name=user.second_name
            ))
        await session.commit()

async def get_user_by_id(user_id:int):
    async with session_factory() as session:
        user = await session.get(Users_orm,user_id)
        return user
    
async def get_users(pagination:PaginationDep):
    async with session_factory() as session:
        query = (select(Users_orm)
        .limit(limit=pagination.limit)
        .offset(offset=((pagination.page+1)*pagination.limit - pagination.limit)))
        result = await session.execute(query)
        return result.scalars().all()
    
async def delete_user(user_id:int):
    async with session_factory() as session:
        stmt = (delete(Users_orm)
        .filter_by(id=user_id))
        await session.execute(stmt)
