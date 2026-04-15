from jose import JWTError,jwt
from fastapi import HTTPException
from src.config import settings
from src.dao.users import Users
import datetime

async def verify_token(token):
    if not token:
        raise HTTPException(status_code=404, detail="Нет токена")
    try:
        jwtoken = jwt.decode(token=token,key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        exp = str(jwtoken.get("exp"))
        if not exp or int(exp) < datetime.datetime.now(datetime.timezone.utc).timestamp():
            raise HTTPException(status_code=401, detail="Нет прав")
        user = await Users.find_one_or_none_by_id(jwtoken.get("user"))
        if not user:
            raise HTTPException(status_code=401, detail="Нет прав")
        return user
    except JWTError as _ex:
        raise HTTPException(status_code=401, detail=_ex)