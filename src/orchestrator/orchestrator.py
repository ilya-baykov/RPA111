import json
import os
from dataclasses import asdict
from typing import Optional

from config.constants.urls import CREATE_TASK_URL
from src.orchestrator.dataclasses_collection import Task
from src.request_manager import RequestManager


class TaskOrchestrator:
    """Класс для работы с задачами в оркестраторе"""
    BASE_URL = CREATE_TASK_URL
    HEADERS = {
        'Content-type': 'application/json',
        'Accept': 'text/plain',
        'Authorization': f'Bearer {os.getenv("TOKEN")}'
    }

    @staticmethod
    def create(name: str, queue_guid: str,
               description: Optional[str] = None, comment: Optional[str] = None, deadline: Optional[str] = None,
               retries: Optional[int] = None, tags: Optional[str] = None, parameters: Optional[dict] = None) -> None:
        """
        Метод для создания задачи
        :param name: Имя задачи
        :param queue_guid: guid очереди, в которую будет добавляться задача
        :param description: описание
        :param comment: комментарий
        :param deadline: дедлайн для создания задачи
        :param retries: количество попыток
        :param tags: Теги
        :param parameters: Параметры
        :return:
        """

        task = Task(
            name=name, queue_guid=queue_guid, parameters=parameters,
            description=description, comment=comment, deadline=deadline, retries=retries, tags=tags)

        # Сериализация параметров задачи в JSON
        data = json.dumps(task.get_dict)

        # Запрос на создание задачи
        RequestManager.post_response(url=TaskOrchestrator.BASE_URL, headers=TaskOrchestrator.HEADERS,
                                     verify=False, data=data,
                                     logger_message=f"Запрос на создание задачи {name}: в очереди:{queue_guid}")
