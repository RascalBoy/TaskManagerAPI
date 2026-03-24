from src.database import session_factory
from src.models.models_orm import Comments_orm,Projects_orm,User_Projects_orm
from src.dto.comments import CommentsCreateDTO, CommentsEditDTO

from sqlalchemy import alias, and_, select
from sqlalchemy.orm import selectinload

async def get_comments():
    async with session_factory() as session:
        query =(
            select(Comments_orm)
        )
        res = await session.execute(query)
        return res.scalars().all()

async def create_comment(comment:CommentsCreateDTO):
    async with session_factory() as session:        
        query = (
            select(User_Projects_orm)
            .select_from(User_Projects_orm)
            .where(User_Projects_orm.user_id == comment.user_id)
        )

        res = await session.execute(query)
        if res.one_or_none is None:
            return "Проекта не существует или отсутствуют права пользователя"
        
        try:
            new_task = Comments_orm(
                    title=comment.title,
                    description=comment.description,
                    user_id=comment.user_id,
                    task_id=comment.task_id
            )
            
            session.add(new_task)
            await session.commit()
            return "Коментарий создан"
        except Exception as _ex:
            return f"Проекта не существует или отсутствуют права пользователя"
        
async def edit_comment(comment_id:int,user_id:int,comment:CommentsEditDTO):
    async with session_factory() as session:
        old_comment = await session.get(Comments_orm,comment_id)
        if old_comment is None:
            return "Коментария для изменения не существует"
        if old_comment.user_id != user_id:
            return "Нет прав для редактирования комментария"
        
        changes = []

        if old_comment.title != comment.title:
            old_comment.title = comment.title
            changes.append("title")
        
        if old_comment.description != comment.description:
            old_comment.description = comment.description
            changes.append("description")
        
        if len(changes) > 0:
            await session.commit()
            return f"Коментарий изменен по следующим параметрам {changes}"
        
        return f"Изменений нет"
    
async def delete_comment(comment_id:int, user_id:int):
    async with session_factory() as session:
        comment = await session.get(Comments_orm,comment_id)
        if comment is None:
            return "Коментария для удаления не существует"
        
        if comment.user_id != user_id:
            return "Ошбибка доступа"
        
        await session.delete(comment)
        await session.commit()
        return "Коментарий успешно удален"
        


        
        
