from fastapi import APIRouter, Depends
from src.orm.tasks_orm import get_tasks
from src.schemas.other import PaginationDep
from src.schemas.tasks import STaskCreate
from typing import Annotated

router = APIRouter()

STaskCreateDep = Annotated[STaskCreate,Depends(STaskCreate)]

@router.get("/v1/tasks", response_model=STaskCreate)
async def show(pagination:PaginationDep):
    res = await show(pagination)
    return {"data":res}

@router.post("/v1/tasks",response_model=STaskCreate)
async def add():
    return {"data":"Not Imlemented"}