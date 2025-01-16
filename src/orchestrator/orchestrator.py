import json
import os
from dataclasses import asdict
from typing import Optional

from config.constants.urls import CREATE_TASK_URL
from src.orchestrator.dataclasses_collection import Task


class Orchestrator:
    """����� ��� ������ � Orchestrator Api """

    @staticmethod
    def create_task():
        """����� ��� �������� ����� � �������"""
        ...


class TaskOrchestrator:
    """����� ��� ������ � �������� � ������������"""
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
        ����� ��� �������� ������
        :param name: ��� ������
        :param queue_guid: guid �������, � ������� ����� ����������� ������
        :param description: ��������
        :param comment: �����������
        :param deadline: ������� ��� �������� ������
        :param retries: ���������� �������
        :param tags: ����
        :param parameters: ���������
        :return:
        """

        task = Task(
            name=name, queue_guid=queue_guid, parameters=parameters,
            description=description, comment=comment, deadline=deadline, retries=retries, tags=tags)

        # ������������ ���������� ������ � JSON
        data = json.dumps(asdict(task))
