from pydantic import BaseModel, ConfigDict,Field
from typing import Annotated

class CommentsCreateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title:str
    description:str
    user_id:int
    task_id:int

class CommentsEditDTO(BaseModel):
    title:str
    description:str

class CommentsDTO(CommentsCreateDTO):
    id:int