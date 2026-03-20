from pydantic import Field, BaseModel
from fastapi import Depends
from typing import Annotated

class PaginationParams(BaseModel):
    limit:int = Field(5,ge=0,lt=100,description="Кол-во элементов на странице")
    page:int = Field(0,ge=0,description="Страница")

PaginationDep = Annotated[PaginationParams,Depends(PaginationParams)]