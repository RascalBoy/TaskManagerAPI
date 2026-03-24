from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated
from src.dto.tasks import TaskRelDTO
from src.dto.comments import CommentsDTO
 
class ProjectCreateDTO(BaseModel):
    title:Annotated[str,Field(title="Project Title")]
    owner_id:Annotated[int,Field(title="Project Owner")]
    
    model_config = ConfigDict(from_attributes=True)

class ProjectDTO(ProjectCreateDTO):
    id:Annotated[int, Field(title="Номер проекта")]

class ProjectRelDTO(ProjectDTO):
    model_config = ConfigDict(from_attributes=True)
    tasks: list["TaskRelDTO"] = []