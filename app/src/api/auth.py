from fastapi import APIRouter,HTTPException, Response,status
from src.orm.users_orm import auth_user
from src.dto.users import UserReadDTO
from src.modules.hash_tools import verify_hash
from src.jwt.token_creator import create_access_token

router = APIRouter(tags=["Auth"])

@router.patch("/v1/auth")
async def login(response:Response,login:str, password:str):
    user = await auth_user(login,password)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такого пользователя не существует")
    
    if not verify_hash(password, user.password):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Отказано в доступе")
    
    token = create_access_token({"user":user.id})
    response.set_cookie("auth_token",token,httponly=True)
    return token
    