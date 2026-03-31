from jose import jwt
import datetime
from datetime import timedelta

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.UTC) + timedelta(hours=1)
    to_encode.update({"exp":expire})
    token = jwt.encode(to_encode,"","HS256")
    return token
