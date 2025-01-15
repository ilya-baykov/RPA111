import os
from typing import Optional

import requests
import urllib3
from requests import Response
from requests.auth import HTTPBasicAuth

from config.constants.paths import SAVE_PATH
from config.logger import logger

# Отключаем предупреждения
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DataDownloader:
    """Класс для загрузки файла из витрины"""
    _AUTH = HTTPBasicAuth(os.getenv('LOGIN'), os.getenv('PASSWORD'))
    BASE_URL = "https://reports.ossdep.rt.ru/api/download"

    @staticmethod
    def _get_response(url: str, _params: dict, logger_message: str) -> Optional[Response]:
        """Отправление запроса к витрине"""
        try:
            response = requests.get(
                url=url,
                auth=DataDownloader._AUTH,
                headers={"Accept-Encoding": "gzip"},
                params=_params,
                verify=False
            )
            response.raise_for_status()  # Проверяем статус ответа
            logger.debug(f"{logger_message}. Статус - {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"{logger_message}. Произошла ошибка: {e}")
            return None

    @staticmethod
    def download_data(params, output_file_name, save_path=SAVE_PATH):
        """Сохранение данных из витрины в виде таблицы"""
        response = DataDownloader._get_response(url=DataDownloader.BASE_URL, _params=params,
                                                logger_message="Запрос на получение данных")

        if response and response.content:
            full_path_file = os.path.join(save_path, output_file_name)  # Полный путь к файлу
            with open(full_path_file, 'wb') as f:  # Сохраняем ответ в файл
                f.write(response.content)
            logger.info(f"Файл {full_path_file} успешно сохранен.")
