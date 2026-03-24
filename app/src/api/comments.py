from typing import Annotated

from src.orm.comments_orm import get_comments, create_comment, edit_comment, delete_comment
from src.dto.comments import CommentsCreateDTO, CommentsEditDTO

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

@router.put("/v1/comments")
async def edit(comment_id:int,user_id:int,comment:CommentsEditDTO):
    try:
        result = await edit_comment(comment_id,user_id,comment)
        return {"status":"success", "data":result}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")
    
@router.delete('/v1/comments')
async def delete(comment_id:int, user_id:int):
    try:
        result = await delete_comment(comment_id, user_id)
        return {"status":"success","data":result}
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"Ошибка {_ex}")

