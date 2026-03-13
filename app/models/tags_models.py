from pydantic import BaseModel,Field
from typing import Annotated

class MTagCreate(BaseModel):
    title:Annotated[str,Field(title="",description="")]

class MTagRead(BaseModel):
    id:Annotated[int,Field(title="",description="")]

class MTagDelete(BaseModel):
    id:Annotated[int,Field(title="",description="")]