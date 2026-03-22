from fastapi import APIRouter, HTTPException,Depends
from src.orm.users_orm import create_user, get_user_by_id,get_users,delete_user,change_user_password
from src.schemas.users import SUserRead,SUserCreate
from typing import Optional,Annotated
from src.schemas.other import PaginationDep

SUserCreateDep = Annotated[SUserCreate,Depends(SUserCreate)]
router = APIRouter()

@router.get("/users",response_model=dict[str,list[SUserRead]])
async def show(pagination:PaginationDep):
    users = await get_users(pagination)
    return {'users':users}

@router.get("/users/{user_id}",response_model=dict[str,SUserRead])
async def show_by_id(user_id:int):
    user = await get_user_by_id(user_id)
    return {"user":user}

@router.post("/users")
async def add(user:SUserCreateDep)->dict[str,SUserCreate|str|None]:
    try:
        await create_user(user)
        return {"status":"Completed", "user":user}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"Не удалось создать пользователя {_ex}")
    

@router.delete("/users")
async def delete(user_id:int):
    if user_id and user_id > 0:
        try:
            await delete_user(user_id=user_id)
        except Exception as _ex:
            raise HTTPException(status_code=500, detail=f"Удаление не удалось {_ex}")
    raise HTTPException(status_code=404, detail="Пользователя для удаления не существует")

@router.patch("/users/change_pass")
async def change_password(user_id:int, new_pass:str):
    res = await change_user_password(user_id,new_pass)
    if not res:
        raise HTTPException(status_code=404, detail="Такого пользователя не существует")
    
    return {'data':res}