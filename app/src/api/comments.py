from typing import Annotated

from src.orm.comments_orm import get_comments, create_comment
from src.dto.comment import CommentsCreateDTO

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

CommentsCreateDTODep = Annotated[CommentsCreateDTO,Depends(CommentsCreateDTO)]

@router.get("/v1/comments")
async def show():
    try:
        result = await get_comments()
        return {"status":"success","data":result}        
    except Exception as _ex:
        return {"status":"success","data":f"{_ex}"}
    
@router.post("/v1/comments")
async def add(comment:CommentsCreateDTO):
    result = await create_comment(comment)
    return {"status":"success", "data":result}