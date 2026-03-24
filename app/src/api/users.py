from fastapi import APIRouter, HTTPException,Depends
from src.orm.users_orm import create_user, get_user_by_id,get_users,delete_user,change_user_password
from src.dto.users import UserReadDTO,UserCreateDTO, UserRelDTO
from typing import Optional,Annotated
from src.dto.other import PaginationDep

UserCreateDTODep = Annotated[UserCreateDTO,Depends(UserCreateDTO)]

router = APIRouter()

@router.get("/v1/users")
async def show(pagination:PaginationDep) -> dict[str,list[UserRelDTO]]:
    users = await get_users(pagination)
    return {'users':users}

@router.get("/v1/users/{user_id}")
async def show_by_id(user_id:int)->dict[str,UserRelDTO]:
    user = await get_user_by_id(user_id)
    return {'users':user}

@router.post("/v1/users")
async def add(user:UserCreateDTODep):
    try:
        await create_user(user)
        return {"status":"Completed", "user":user}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"Не удалось создать пользователя {_ex}")
    
@router.delete("/v1/users")
async def delete(id:int):
    if id > 0:
        try:
            await delete_user(user_id=id)
        except Exception as _ex:
            raise HTTPException(status_code=500, detail=f"Удаление не удалось {_ex}")
    else:
        raise HTTPException(status_code=404, detail="Пользователя для удаления не существует")

@router.patch("/v1/users")
async def change_password(user_id:int, new_pass:str):
    res = await change_user_password(user_id,new_pass)
    if not res:
        raise HTTPException(status_code=404, detail="Такого пользователя не существует")
    
    return {'data':res}