from typing import Annotated,Optional
from pydantic import BaseModel,Field,ConfigDict
from datetime import datetime

from src.models.models_orm import Complition_state

class TaskCreateDTO(BaseModel):
    title: Annotated[str, Field(title="",description="")]
    description: Annotated[str, Field(title="",description="")]
    completion_state: Annotated[Complition_state,Field(title="",description="")]
    project_id: Annotated[int,Field(title="",description="")]

    model_config=ConfigDict(from_attributes=True)

class TaskDTO(TaskCreateDTO):
    model_config = ConfigDict(from_attributes=True)
    id:Annotated[int,Field(title="Номер задачи")]
