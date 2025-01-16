from typing import Optional, Any

import requests
import urllib3

from config.logger import logger

urllib3.disable_warnings()


class GetRequestManager:
    """Класс для управления HTTP-запросами"""

    @staticmethod
    def get_response(url: str, logger_message: str,
                     auth: Any = None,
                     headers: Optional[dict[str, str]] = None,
                     params: Optional[dict[str, Any]] = None,
                     data: Optional[dict[str, Any]] = None,
                     verify: bool = False) -> Optional[requests.Response]:

        """Отправление GET-запроса к витрине"""

        try:
            response = requests.get(
                url=url,
                auth=auth,
                headers=headers,
                params=params,
                data=data,
                verify=verify)

            response.raise_for_status()  # Проверяем статус ответа
            logger.debug(f"{logger_message}. Статус - {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"{logger_message}. Произошла ошибка: {e}")
            return None
