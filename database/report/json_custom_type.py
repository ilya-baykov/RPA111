import json

from sqlalchemy.types import TypeDecorator, Text


class JSONEncodedDict(TypeDecorator):
    """
    Настраиваемый тип для хранения Python-объектов (словарей, списков и т.д.)
    в виде текстового JSON в базе данных.

    Этот тип автоматически преобразует объекты Python в строковый формат JSON
    при записи в базу данных и обратно при чтении. Кодировка Unicode не экранируется,
    чтобы сохранить данные в читаемом виде.
    """
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return json.dumps(value, ensure_ascii=False)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return json.loads(value)
