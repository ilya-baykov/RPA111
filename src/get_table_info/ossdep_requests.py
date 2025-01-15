import os
from typing import Optional

import requests
import urllib3
from requests import Response
from requests.auth import HTTPBasicAuth

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
    def download_data(_params, _output_file):
        """Сохранение данных из витрины в виде таблицы"""
        response = DataDownloader._get_response(url=DataDownloader.BASE_URL, _params=_params,
                                                logger_message="Запрос на получение данных")

        if response and response.content:
            with open(_output_file, 'wb') as f:  # Сохраняем ответ в файл
                f.write(response.content)
            logger.info("Файл успешно сохранен.")
