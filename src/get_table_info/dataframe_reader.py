import json
from typing import Optional

import pandas as pd

from config.logger import logger


class DataFrameReader:
    """Класс для считывания файла с витрины"""

    def __init__(self, file_path: str):
        """
        Инициализация
        :param file_path: Полный путь до файла
        """
        self.file_path = file_path

    def _read_data(self) -> str:
        """Считывание файла и получение его содержимого"""
        try:
            with open(file=self.file_path, mode='r') as file:
                file_content = file.read()
                logger.debug(f"Получено содержимое из файла: {self.file_path}")
                return file_content
        except Exception as e:
            logger.error(f"Ошибка при считывании файла: {self.file_path} - {e}")

    def get_file_dataframe(self) -> pd.DataFrame:
        """Получение DataFrame из файла"""
        file_content: Optional[str] = self._read_data()

        if file_content is None:
            return pd.DataFrame()  # Возвращаем пустой DataFrame в случае ошибки

        try:
            data = json.loads(file_content)  # Парсим JSON
            columns = data['columns']  # Получаем названия колонок
            table_data = data['table_data']  # Получаем данные таблицы

            # Создаем DataFrame
            df = pd.DataFrame(table_data, columns=columns)
            return df

        except Exception as e:
            logger.error(f"Ошибка при создании DataFrame: {e}")
            return pd.DataFrame()  # Возвращаем пустой DataFrame в случае ошибки
