import json
import os
from dataclasses import asdict
from typing import Optional

from config.constants.urls import CREATE_TASK_URL
from src.orchestrator.dataclasses_collection import Task


class Orchestrator:
    """Класс для работы с Orchestrator Api """

    @staticmethod
    def create_task():
        """Метод для создания задач в очереди"""
        ...


class TaskOrchestrator:
    """Класс для работы с задачами в оркестраторе"""
    BASE_URL = CREATE_TASK_URL
    HEADERS = {
        'Content-type': 'application/json',
        'Accept': 'text/plain',
        'Authorization': f'Bearer {os.getenv("TOKEN")}'
    }

    def create(self, name: str, queue_guid: str,
               description: Optional[str], comment: Optional[str], deadline: Optional[str],
               retries: Optional[int], tags: Optional[str], parameters: Optional[dict]):
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
        data = json.dumps(asdict(task))
