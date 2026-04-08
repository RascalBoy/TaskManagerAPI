from src.dto.projects import ProjectCreateDTO
from src.modules.hash_tools import get_hash
from src.models.models_orm import Projects_orm
from src.database import session_factory
from src.dao.user_projects import User_Projects
from src.dto.user_projects import SUserProjectCreate
from src.dao.base import BaseDAO

class Projects(BaseDAO):
    model = Projects_orm

    @classmethod
    async def insert(cls, object):
        project = await super().insert(object)
        await User_Projects.add_user(project.owner_id,project.id)
