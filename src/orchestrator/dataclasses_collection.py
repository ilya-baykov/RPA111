from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    name: str  # ��� ������
    queue_guid: str  # guid �������, � ������� ����� ����������� ������
    description: Optional[str]  # ��������
    comment: Optional[str]  # �����������
    deadline: Optional[str]  # ������� ��� �������� ������
    retries: Optional[int]  # ���������� �������
    tags: Optional[list]  # ����
    parameters: Optional[dict]  # ���������
