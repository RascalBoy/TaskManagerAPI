from pydantic import BaseModel,Field
from typing import Annotated

class UserCreate(BaseModel):
    login: Annotated[str, Field(title="Логин пользователя",description="Необходим для регистрации и авторизации в системе", example="test@mail.com")]
    password: Annotated[str,Field(title="Пароль пользователя",description="Необходим для регистрации и авторизации в системе",example="password123")]
    nickname: Annotated[str,Field(title="Никнейм пользователя",description="Необходим для отображения в системе")]
    name: Annotated[str,Field(title="Имя пользователя",description="Необходим для отображения в системе")]
    second_name: Annotated[str,Field(title="Фамилия пользователя",description="Необходим для отображения в системе")]

class UserRead(UserCreate):
    id:Annotated[int, Field(title="Идентификационный номер пользователя",description="")]

class UserDelete(BaseModel):
    id:Annotated[int,Field(title="Идентификационный номер пользователя",description="Необходимы для удаления")]