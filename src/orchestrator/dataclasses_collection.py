from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    name: str  # Имя задачи
    queue_guid: str  # guid очереди, в которую будет добавляться задача
    description: Optional[str]  # описание
    comment: Optional[str]  # комментарий
    deadline: Optional[str]  # дедлайн для создания задачи
    retries: Optional[int]  # количество попыток
    tags: Optional[list]  # Теги
    parameters: Optional[dict]  # Параметры
