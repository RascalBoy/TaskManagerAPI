from jose import JWTError,jwt
from fastapi import HTTPException
from config import settings
from src.dao.users import Users

async def verify_token(token):
    if not token:
        raise HTTPException(status_code=404, detail="Нет токена")
    try:
        jwtoken = jwt.decode(token=token,key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user = await Users.find_one_or_none_by_id(jwtoken.get("user"))
        if not user:
            raise HTTPException(status_code=401, detail="Нет прав")
        return user
    except JWTError as _ex:
        raise HTTPException(status_code=401, detail=_ex)