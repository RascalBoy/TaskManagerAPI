from fastapi import FastAPI,Depends
from typing import List,Dict,Optional,Annotated
import uvicorn
from orm import create_user,create_tables
from models.user_models import MUserCreate,MUserDelete,MUserRead

app = FastAPI()



@app.get("/")
async def index():
    return {"data":"Welcome to TaskManagerAPI by Sergey Marunin"}

@app.get("/users/{user_id}")
async def show_user_by_id(user_id:int) -> int:
    return user_id

@app.get("/users")
async def show_users() ->List[MUserRead]:
    return []

@app.post("/users/add")
async def add_user(user:MUserCreate):
    create_user(user)

if __name__ == "__main__":
    create_tables()
    uvicorn.run(app="main:app",reload=True)