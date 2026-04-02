from fastapi import APIRouter,HTTPException, Response
from src.dao.users import Users
from src.modules.response_creator import ResponseCreator
from src.modules.hash_tools import verify_hash
from src.jwt.token_creator import create_access_token

router = APIRouter(tags=["Аутентификация"])

@router.patch("/v1/auth")
async def login(response:Response, user_login:str, user_password:str):
    user = await Users.find_one_or_none(login=user_login)
    if not user:
        raise HTTPException(status_code=404, detail="Такого пользователя не существует")
    
    if not verify_hash(user_password, user.password):
        return HTTPException(status_code=401,detail="Отказано в доступе")
    
    token = create_access_token({"user":user.id})
    response.set_cookie("auth_token",token,httponly=True)
    return ResponseCreator.create_response(object=token,
                                           message="Аутентификация выполнена успешно")
    