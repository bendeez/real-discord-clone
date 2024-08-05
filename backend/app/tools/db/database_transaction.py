from fastapi import Depends
from app.tools.db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class DatabaseTransactionService:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db

    async def create(self, model, **attributes):
        model_instance = model(**attributes)
        self.db.add(model_instance)
        await self.db.commit()
        await self.db.refresh(model_instance)
        return model_instance

    async def get_all(self, model):
        models = await self.db.execute(select(model))
        return models.scalars().all()
