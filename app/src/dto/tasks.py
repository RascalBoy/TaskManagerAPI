from typing import Annotated,Optional
from pydantic import BaseModel,Field,ConfigDict
from datetime import datetime

from src.models.models_orm import Complition_state
from src.dto.comments import CommentsDTO

class TaskCreateDTO(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    
    title: Annotated[str, Field(title="",description="")]
    description: Annotated[str, Field(title="",description="")]
    completion_state: Annotated[Complition_state,Field(title="",description="")]
    project_id: Annotated[int,Field(title="",description="")]


class TasksDTO(TaskCreateDTO):
    id:Annotated[int,Field(title="Номер задачи")]
    created_at:datetime
    updated_at:datetime

class TaskRelDTO(TasksDTO):
    comments:list["CommentsDTO"] = []
