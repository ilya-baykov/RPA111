import os

from requests.auth import HTTPBasicAuth

from config.logger import logger
from config.constants.paths import SAVE_PATH
from config.constants.urls import SHOWCASE_DOWNLOAD_URL
from src.request_manager import RequestManager


class ShowCase:
    """Класс для работы с витриной"""
    _AUTH = HTTPBasicAuth(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    def __init__(self, table_name: str):
        """
        Инициализация
        :param table_name:  Имя таблицы витрины
        """

        self.table_name = table_name

    def download_table_dataframe(self, output_file_name: str, save_path=SAVE_PATH):
        """Метод для загрузки данных с витрины в файл

        Сохранение данных из витрины в виде таблицы
        :param output_file_name: Имя файла после загрузки
        :param save_path: Путь для сохранения файла с данными
        :return: При успешной загрузке данных возвращается полный путь до файла
        """

        params = {'table': self.table_name}
        response = RequestManager.get_response(url=SHOWCASE_DOWNLOAD_URL, params=params, auth=self._AUTH,
                                               logger_message=f"Запрос на загрузку данных"
                                                              f" из витрины {self.table_name}")

        if response and response.content:
            full_path_file = os.path.join(save_path, output_file_name)  # Полный путь к файлу
            with open(full_path_file, 'wb') as f:  # Сохраняем ответ в файл
                f.write(response.content)
            logger.info(f"Файл {full_path_file} успешно сохранен.")
            return str(full_path_file)


showcase = ShowCase(table_name='cons_dm.wfm_ppr_outsherpa')
