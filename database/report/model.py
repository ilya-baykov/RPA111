from enum import Enum

from sqlalchemy import Column, String, Integer, Text, DateTime

from database.report.json_custom_type import JSONEncodedDict
from database.core import BaseCandidatesDb


class Report(BaseCandidatesDb):
    __tablename__ = 'report'
    __table_args__ = {'schema': 'public'}  # Укажите схему

    id = Column(Integer, primary_key=True, autoincrement=True)

    mrf = Column(String, primary_key=True, autoincrement=True)  # Макрорегион (mrf)
    gid = Column(Integer, nullable=True)  # ИД_ОРПОН (gid)
    address = Column(String, nullable=True)  # Адрес (adres)
    type_network = Column(String, nullable=True)  # Тип Сети (s_type_network)
    device_manufacturer = Column(String, nullable=True)  # Производитель (proizvoditel_ustroystva)
    device_model = Column(String, nullable=True)  # Модель (model)
    device_id = Column(Integer, nullable=True)  # ИД Устройства (device_id)
    hostname = Column(String, nullable=True)  # Имя хоста (host_name)
    jobs_type = Column(String, nullable=True)  # Тип Работы (s_type_work)
    eqm_number = Column(Integer, nullable=True)  # Номер EQM (eqm_num)

    # НЕИЗВЕСТНЫЕ ПОЛЯ
    network_incident = Column(Integer, nullable=True)  # СетевойИнцидент (???)
    jobs = Column(String, nullable=True)  # Работы ( ??? )
    number_sypr = Column(Integer, nullable=True)  # НомерСУПР (???)
    ppr_date = Column(DateTime, nullable=True)  # Дата Работ (ppr_date)
    typical_tc = Column(String, nullable=True)  # Типовая ТК ( ??? )

    # Формирует Скрипт (ВОЗМОЖНО)
    ppr = Column(Integer, nullable=True)  # ППР (ФОРМИРУЕТ СКРИПТ)
    status = Column(String, nullable=True)  # Статус Обработки (ФОРМИРУЕТ СКРИПТ)
    processing_date = Column(DateTime, nullable=True)  # Дата обработки (ФОРМИРУЕТ СКРИПТ)
    error_description = Column(String, nullable=True)  # Описание ошибки (ФОРМИРУЕТ СКРИПТ)
