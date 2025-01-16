from typing import Optional, Any, Callable

import requests
import urllib3

from config.logger import logger

urllib3.disable_warnings()


class RequestManager:
    """Класс для управления HTTP-запросами"""

    @staticmethod
    def _send_request(method: Callable, url: str, logger_message: str,
                      auth: Any = None,
                      headers: Optional[dict[str, str]] = None,
                      data: Optional[dict[str, Any]] = None,
                      params: Optional[dict[str, Any]] = None,
                      verify: bool = False) -> Optional[requests.Response]:
        """Отправление HTTP-запроса"""

        try:
            response = method(url=url, auth=auth, headers=headers, data=data, params=params, verify=verify)
            response.raise_for_status()  # Проверяем статус ответа
            logger.debug(f"{logger_message}. Статус - {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"{logger_message}. Произошла ошибка: {e}")
            return None

    @staticmethod
    def get_response(url: str, logger_message: str,
                     auth: Any = None,
                     headers: Optional[dict[str, str]] = None,
                     params: Optional[dict[str, Any]] = None,
                     verify: bool = False) -> Optional[requests.Response]:

        """Отправление GET-запроса к витрине"""
        return RequestManager._send_request(
            method=requests.get, url=url,
            auth=auth, headers=headers, params=params, verify=verify,
            logger_message=logger_message)

    @staticmethod
    def post_response(url: str, logger_message: str,
                      auth: Any = None,
                      headers: Optional[dict[str, str]] = None,
                      data: Optional[dict[str, Any]] = None,
                      verify: bool = False) -> Optional[requests.Response]:

        """Отправление POST-запроса к витрине"""
        return RequestManager._send_request(
            method=requests.post,
            url=url, auth=auth, headers=headers, data=data, verify=verify,
            logger_message=logger_message)
