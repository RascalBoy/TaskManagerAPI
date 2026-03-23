from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated

class SProjectCreate(BaseModel):
    title:Annotated[str,Field(title="Project Title")]
    owner_id:Annotated[int,Field(title="Project Owner")]
    
    model_config = ConfigDict(from_attributes=True)