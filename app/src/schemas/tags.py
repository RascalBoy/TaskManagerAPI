from pydantic import BaseModel,Field
from typing import Annotated

class STagCreate(BaseModel):
    title:Annotated[str,Field(title="",description="")]

class STagRead(STagCreate):
    id:Annotated[int,Field(title="",description="")]

class STagDelete(BaseModel):
    id:Annotated[int,Field(title="",description="")]