from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from database.settings import db_candidates_settings

from config.logger import logger


class BaseCandidatesDb(DeclarativeBase):
    pass


class DataBase:
    def __init__(self, settings):
        self.db_host = settings.DB_HOST
        self.db_user = settings.DB_USER
        self.db_password = settings.DB_PASSWORD
        self.db_name = settings.DB_NAME
        self.db_connect = settings.DATABASE_URL

        self.async_engine = create_async_engine(self.db_connect)
        self.Session = async_sessionmaker(bind=self.async_engine, class_=AsyncSession)

    async def create_db(self, base):
        # Убедитесь, что метаданные содержат ваши модели
        logger.info(f"Метаданные: {base.metadata.tables.keys()}")

        async with self.async_engine.begin() as connect:
            await connect.run_sync(base.metadata.create_all)
        logger.info("Таблица созданы")

    async def reset_database(self, base):
        async with self.async_engine.begin() as connect:
            await connect.run_sync(base.metadata.drop_all)
        logger.info("БД очищена")

    async def reflect_tables(self, base, schema: str):
        """Загружает метаданные для существующих таблиц в указанной схеме."""
        async with self.async_engine.begin() as connect:
            await connect.run_sync(base.metadata.reflect, schema=schema)
        logger.info(f"Загружены таблицы из схемы: {schema}")


db_candidates = DataBase(db_candidates_settings)
