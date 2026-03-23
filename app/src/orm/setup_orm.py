from src.database import Base,engine

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_tables():
     async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


