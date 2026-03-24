from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated

class SUserProjectCreate(BaseModel):
    user_id:Annotated[int,Field(title="User")]
    project_id:Annotated[int,Field(title="Project")]
    model_config = ConfigDict(from_attributes=True)