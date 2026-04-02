from src.dto.users import UserCreateDTO
from src.modules.hash_tools import get_hash
from src.models.models_orm import Tasks_orm
from src.database import session_factory
from src.dao.base import BaseDAO

class Tasks(BaseDAO):
    model = Tasks_orm