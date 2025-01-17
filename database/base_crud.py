from sqlalchemy import select
from database.core import DataBase
from config.logger import logger
from typing import Optional, List, Any


class BaseCRUD:
    model = None
    schema: str = 'public'
    db: DataBase = None

    @classmethod
    async def find_by_id(cls, model_id: int) -> Optional[Any]:
        """Находит запись по ID.

        Args:
            model_id (int): ID записи.

        Returns:
            Объект модели или None, если запись не найдена.
        """
        try:
            async with cls.db.Session() as session:
                query = select(cls.model).filter_by(id=model_id).execution_options(schema=cls.schema)
                result = await session.execute(query)
                return result.scalar_one_or_none()
        except Exception as e:
            logger.error(f"Ошибка при поиске записи по ID {model_id}: {e}")
            return None

    @classmethod
    async def find_one_or_none(cls, **filter_by: Any) -> Optional[Any]:
        """Находит одну запись по заданным фильтрам.

        Args:
            **filter_by: Параметры для фильтрации.

        Returns:
            Объект модели или None, если запись не найдена.
        """
        try:
            async with cls.db.Session() as session:
                query = select(cls.model).filter_by(**filter_by).execution_options(schema=cls.schema)
                result = await session.execute(query)
                return result.scalar_one_or_none()
        except Exception as e:
            logger.error(f"Ошибка при поиске записи с фильтрами {filter_by}: {e}")
            return None

    @classmethod
    async def find_all(cls, **filter_by: Any) -> List[Any]:
        """Находит все записи по заданным фильтрам.

        Args:
            **filter_by: Параметры для фильтрации.

        Returns:
            Список объектов модели, соответствующих фильтрам.
        """
        try:
            async with cls.db.Session() as session:
                query = select(cls.model).filter_by(**filter_by).execution_options(schema=cls.schema)
                result = await session.execute(query)
                return result.scalars().all()
        except Exception as e:
            logger.error(f"Ошибка при поиске всех записей с фильтрами {filter_by}: {e}")
            return []

    @classmethod
    async def create(cls, **kwargs: Any) -> Optional[Any]:
        """Создает новую запись в базе данных.

        Args:
            **kwargs: Параметры для создания новой записи.

        Returns:
            Объект созданной модели.
        """
        try:
            async with cls.db.Session() as session:
                new_row = cls.model(**kwargs)
                session.add(new_row)
                await session.commit()
                await session.refresh(new_row)
                return new_row
        except Exception as e:
            logger.error(f"Ошибка при создании новой записи: {e}")
            return None

    @classmethod
    async def update_row(cls, model_id: int, **kwargs: Any) -> Optional[Any]:
        """Обновляет запись по ID.

        Args:
            model_id (int): ID записи для обновления.
            **kwargs: Параметры для обновления записи.

        Returns:
            Объект обновленной модели или None, если запись не найдена.
        """
        try:
            async with cls.db.Session() as session:
                query = select(cls.model).filter_by(id=model_id).execution_options(schema=cls.schema)
                result = await session.execute(query)
                row_to_update = result.scalar_one_or_none()

                if row_to_update is None:
                    logger.warning(f"Запись с ID {model_id} не найдена для обновления.")
                    return None

                # Обновляем поля записи
                for key, value in kwargs.items():
                    setattr(row_to_update, key, value)

                # Сохраняем изменения
                await session.commit()
                return row_to_update  # Возвращаем обновленный экземпляр
        except Exception as e:
            logger.error(f"Ошибка при обновлении записи с ID {model_id}: {e}")
            return None
