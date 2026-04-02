from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated
from src.dto.projects import ProjectRelDTO

class UserCreateDTO(BaseModel):
    login: Annotated[str, Field(title="Логин пользователя",
    description="Необходим для регистрации и авторизации в системе")]
    password: Annotated[str,Field(title="Пароль пользователя",
    description="Необходим для регистрации и авторизации в системе")]
    nickname: Annotated[str,Field(title="Никнейм пользователя",description="Необходим для отображения в системе")]
    name: Annotated[str,Field(title="Имя пользователя",description="Необходим для отображения в системе")]
    second_name: Annotated[str,Field(title="Фамилия пользователя",description="Необходим для отображения в системе")]

class UserReadDTO(BaseModel):
    id:Annotated[int, Field(title="Идентификационный номер пользователя",description="")]
    login: Annotated[str, Field(title="Логин пользователя",
    description="Необходим для регистрации и авторизации в системе")]
    nickname: Annotated[str,Field(title="Никнейм пользователя",description="Необходим для отображения в системе")]
    name: Annotated[str,Field(title="Имя пользователя",description="Необходим для отображения в системе")]
    second_name: Annotated[str,Field(title="Фамилия пользователя",description="Необходим для отображения в системе")]

class UserRelDTO(UserReadDTO):
    
    model_config = ConfigDict(from_attributes=True)
    projects: list["ProjectRelDTO"] = []