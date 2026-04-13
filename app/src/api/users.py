from fastapi import APIRouter, HTTPException,Depends
from src.models.models_orm import Projects_orm, Tasks_orm, Users_orm
from sqlalchemy.orm import selectinload
from src.modules.hash_tools import get_hash
from src.dao.users import Users
from src.dto.users import UserCreateDTO, UserRelDTO
from src.dto.other import PaginationDep
from src.modules.response_creator import ResponseCreator

from typing import Annotated
UserCreateDTODep = Annotated[UserCreateDTO,Depends(UserCreateDTO)]

router = APIRouter(prefix="/users",tags=["Пользователи"])

@router.get("/v1/")
async def show(pagination:PaginationDep):
    users = await Users.find_all(pagination=pagination,
                                options=[selectinload(Users_orm.projects)
                                .selectinload(Projects_orm.tasks)
                                .selectinload(Tasks_orm.comments)])
    if not users:
        raise HTTPException(status_code=404, detail="Пользователей нет")
    _users = [UserRelDTO.model_validate(row,from_attributes=True) for row in users]
    return ResponseCreator.create_response(_users)#type:ignore

@router.get("/v1/{user_id}")
async def show_by_id(user_id:int):
    user = await Users.find_one_or_none_by_id(user_id, options=[selectinload(Users_orm.projects)
                                                                .selectinload(Projects_orm.tasks)
                                                                .selectinload(Tasks_orm.comments)])
    if not user:
        raise HTTPException(status_code=404, detail="Пользователя не существует")
    
    return ResponseCreator.create_response(object=UserRelDTO.model_validate(user,from_attributes=True))

@router.post("/v1/")
async def add(user:UserCreateDTODep):
        hashed_pass = get_hash(user.password)
        user.password = hashed_pass
        result = await Users.insert(user)
        return ResponseCreator.create_response(message="Пользователь добавлен",object=user)
    
@router.delete("/v1/")
async def delete(id:int):
    try:
        await Users.delete_by_id(model_id=id)
        return ResponseCreator.create_response(message="Пользователь успешно удален")
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"Удаление не удалось {_ex}")

@router.patch("/v1/")
async def change_password(user_id:int, new_pass:str):
    res = await Users.update_column_by_id(Users.model.password,
                                          get_hash(new_pass),id=user_id)
    if not res:
        raise HTTPException(status_code=404, detail="Такого пользователя не существует")
    
    return ResponseCreator.create_response(message="Пароль успешно изменен")