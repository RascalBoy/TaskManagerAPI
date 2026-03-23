from fastapi import APIRouter,HTTPException
from src.orm.users_orm import auth_user
from src.schemas.users import SUserRead

router = APIRouter()

@router.patch("/v1/auth", response_model=dict[str,SUserRead])
async def login(login:str, password:str):
    res = await auth_user(login,password)
    if not res:
        raise HTTPException(status_code=404, detail="Такого пользователя не существует")
    
    return {"data":res}