from typing import Annotated

from pydantic import BaseModel,Field

class MTaskCreate(BaseModel):
    title: Annotated[str, Field(title="",description="")]
    description: Annotated[str, Field(title="",description="")]
    completion_date: str
    completion_state: Annotated[int,Field(title="",description="")]
    project: Annotated[int,Field(title="",description="")]
    tag: Annotated[int,Field(title="",description="")]

class MTaskRead(BaseModel):
    id:Annotated[int,Field(title="",description="")]

class MTaskDelete(BaseModel):
    id:Annotated[int,Field(title="",description="")]