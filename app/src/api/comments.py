from typing import Annotated
from src.dao.comments import Comments
from src.dto.comments import CommentsCreateDTO, CommentsEditDTO, CommentsDTO
from src.modules.response_creator import ResponseCreator
from src.dto.other import PaginationDep
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(tags=["Комментарии"])

CommentsCreateDTODep = Annotated[CommentsCreateDTO,Depends(CommentsCreateDTO)]

@router.get("/v1/comments")
async def show(pagination:PaginationDep):
    try:
        result = await Comments.find_all(pagination)
        return ResponseCreator.create_response(object=[CommentsDTO.model_validate(row, from_attributes=True) for row in result])   
    except Exception as _ex:
        return ResponseCreator.create_response(status="Error", status_code=500, message=f"{_ex}")
    
@router.post("/v1/comments")
async def add(comment:CommentsCreateDTODep):
    result = await Comments.insert(comment)
    return ResponseCreator.create_response(message="Комментарий успешно создан",object=comment)

@router.put("/v1/comments")
async def edit(comment_id:int,user_id:int,comment:CommentsEditDTO):
    try:
        _comment=await Comments.find_one_or_none_by_id(comment_id)
        if not _comment:
            raise HTTPException(404,"Такого коментария не существует")
        if _comment.user_id != user_id:
            raise HTTPException(401,"У вас нет прав на редактирования коментария")
        await Comments.update(comment,id = comment_id,user_id=user_id)
        return ResponseCreator.create_response(message="Комментарий успешно отредактирован",object=comment)
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")
    
@router.delete('/v1/comments')
async def delete(comment_id:int, user_id:int):
    try:
        result = await Comments.delete(id=comment_id, user_id=user_id)
        return ResponseCreator.create_response(message="Комментарий успешно удален",object=[])
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"Ошибка {_ex}")

