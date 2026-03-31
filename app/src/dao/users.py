from src.models.models_orm import Users_orm
from src.dao.base import BaseDAO

class Users(BaseDAO):
    model = Users_orm