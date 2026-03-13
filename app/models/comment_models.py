from pydantic import BaseModel,Field
from typing import Annotated

class MCommentCreate(BaseModel):
    title: Annotated[str,Field(title="",description="")]
    user_id: Annotated[int,Field(title="",description="")]
    project_id: Annotated[int,Field(title="",description="")]

class MCommentRead(MCommentCreate):
    int:Annotated[int,Field(title="",description="")]

class MCommentDelete(BaseModel):
    user_id: Annotated[int,Field(title="",description="")]
    project_id: Annotated[int,Field(title="",description="")]