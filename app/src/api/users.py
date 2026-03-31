from fastapi import APIRouter, HTTPException,Depends
from src.orm.users_orm import create_user, get_user_by_id,change_user_password
from src.dao.users import Users
from src.dto.users import UserReadDTO,UserCreateDTO, UserRelDTO
from typing import Optional,Annotated
from src.dto.other import PaginationDep

UserCreateDTODep = Annotated[UserCreateDTO,Depends(UserCreateDTO)]

router = APIRouter(prefix="/users",tags=["Пользователи"])

@router.get("/v1/")
async def show(pagination:PaginationDep):
    users = await Users.find_all(pagination=pagination)
    return {'users':users}

@router.get("/v1/{user_id}")
async def show_by_id(user_id:int)->dict[str,UserRelDTO]:
    user = await get_user_by_id(user_id)
    return {'users':user}

@router.post("/v1/")
async def add(user:UserCreateDTODep):
    try:
        await create_user(user)
        return {"status":"Completed", "user":user}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"Не удалось создать пользователя {_ex}")
    
@router.delete("/v1/")
async def delete(id:int):
    if id > 0:
        try:
            await Users.delete_by_id(model_id=id)
        except Exception as _ex:
            raise HTTPException(status_code=500, detail=f"Удаление не удалось {_ex}")
    else:
        raise HTTPException(status_code=404, detail="Пользователя для удаления не существует")

@router.patch("/v1/")
async def change_password(user_id:int, new_pass:str):
    res = await change_user_password(user_id,new_pass)
    if not res:
        raise HTTPException(status_code=404, detail="Такого пользователя не существует")
    
    return {'data':res}