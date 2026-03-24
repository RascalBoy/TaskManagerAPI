from pydantic import BaseModel,Field
from typing import Annotated

class SCommentCreate(BaseModel):
    title: Annotated[str,Field(title="",description="")]
    user_id: Annotated[int,Field(title="",description="")]
    project_id: Annotated[int,Field(title="",description="")]

class SCommentRead(SCommentCreate):
    int:Annotated[int,Field(title="",description="")]

class SCommentDelete(BaseModel):
    user_id: Annotated[int,Field(title="",description="")]
    project_id: Annotated[int,Field(title="",description="")]