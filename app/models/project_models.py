from pydantic import BaseModel,Field
from typing import Annotated

class MProjectCreate(BaseModel):
    title:Annotated[str,Field(title="Project Title")]
    project_owner_id:Annotated[str,Field(title="Project Owner")]