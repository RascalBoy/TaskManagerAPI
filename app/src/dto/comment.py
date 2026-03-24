from pydantic import BaseModel,Field
from typing import Annotated

class CommentsCreateDTO(BaseModel):
    title:str
    description:str
    user_id:int
    project_id:int

class CommentsDTO(CommentsCreateDTO):
    id:int