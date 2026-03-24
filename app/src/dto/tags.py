from pydantic import BaseModel, ConfigDict
from typing import Annotated

class TagCreateDTO(BaseModel):
    title:str
    creator_id:int
    task_id:int

class TagDTO(TagCreateDTO):
    id:int
    model_config = ConfigDict(from_attributes=True)