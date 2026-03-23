from typing import Annotated

from pydantic import BaseModel,Field

class STaskCreate(BaseModel):
    title: Annotated[str, Field(title="",description="")]
    description: Annotated[str, Field(title="",description="")]
    completion_date: str
    completion_state: Annotated[int,Field(title="",description="")]
    project_id: Annotated[int,Field(title="",description="")]
    tag_id: Annotated[int,Field(title="",description="")]
