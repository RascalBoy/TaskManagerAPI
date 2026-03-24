from src.database import session_factory
from src.models.models_orm import Comments_orm,Projects_orm
from src.dto.comment import CommentsCreateDTO

from sqlalchemy import select
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
        project = await session.get(Projects_orm, comment.project_id)
        if project is not None:
            return "Такого проекта не существует"
        
        try:
            new_task = Comments_orm(
                    title=comment.title,
                    description=comment.description,
                    user_id=comment.user_id,
                    project_id=comment.project_id
            )
            await session.commit()
            return "Коментарий создан"
        except Exception as _ex:
            return f"{_ex}"
        
