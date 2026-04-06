from src.dto.projects import ProjectCreateDTO
from src.modules.hash_tools import get_hash
from src.models.models_orm import Comments_orm
from src.database import session_factory
from src.dao.base import BaseDAO

class Comments(BaseDAO):
    model = Comments_orm