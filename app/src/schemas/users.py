from pydantic import BaseModel,Field
from typing import Annotated

class SUserCreate(BaseModel):
    login: Annotated[str, Field(title="Логин пользователя",
    description="Необходим для регистрации и авторизации в системе")]
    password: Annotated[str,Field(title="Пароль пользователя",
    description="Необходим для регистрации и авторизации в системе")]
    nickname: Annotated[str,Field(title="Никнейм пользователя",description="Необходим для отображения в системе")]
    name: Annotated[str,Field(title="Имя пользователя",description="Необходим для отображения в системе")]
    second_name: Annotated[str,Field(title="Фамилия пользователя",description="Необходим для отображения в системе")]

class SUserRead(SUserCreate):
    id:Annotated[int, Field(title="Идентификационный номер пользователя",description="")]

class SUserDelete(BaseModel):
    id:Annotated[int,Field(title="Идентификационный номер пользователя",description="Необходимы для удаления")]