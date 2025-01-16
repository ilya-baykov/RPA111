from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    name: str  # Название создаваемой задачи (макс. 256 символов)
    queue_guid: str  # GUID очереди для добавления задачи
    description: Optional[str] = None  # Описание создаваемой задачи
    comment: Optional[str] = None  # Комментарий к создаваемой задаче
    deadline: Optional[str] = None  # Срок выполнения создаваемой задачи
    retries: Optional[int] = None  # Количество попыток для создаваемой задачи
    tags: Optional[list[str]] = None  # Теги для создаваемой задачи, разделенные точкой с запятой
    parameters: Optional[dict] = None  # Параметры в формате JSON

    @property
    def get_dict(self):
        return {
            "Name": self.name,
            "QueueGuid": self.queue_guid,
            "Description": self.description,
            "Comment": self.comment,
            "Deadline": self.deadline,
            "Retries": self.retries,
            "Tags": self.tags,
            "Parameters": self.parameters,
        }
