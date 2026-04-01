from src.dto.users import UserCreateDTO
from src.modules.hash_tools import get_hash
from src.models.models_orm import Users_orm
from src.database import session_factory
from src.dao.base import BaseDAO

class Users(BaseDAO):
    model = Users_orm

    @classmethod
    async def create(cls,user:UserCreateDTO):
        async with session_factory() as session:
            session.add(Users_orm(
                login=user.login,
                password=str(get_hash(user.password)),
                nickname=user.nickname,
                name=user.name,
                second_name=user.second_name
                ))
            await session.commit()