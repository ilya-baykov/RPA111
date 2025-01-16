import config.env_loader  # Необходим для загрузки переменных окружения
import pandas as pd

from src.get_table_info.dataframe_reader import DataFrameReader
from src.orchestrator.orchestrator import TaskOrchestrator
from src.showcase.showcase import showcase


def main() -> None:
    # Загружаем данные из витрины в текстовый файл
    showcase_file_path = showcase.download_table_dataframe(output_file_name='showcase.txt')

    # Считываем текстовый файл с данными из витрины и формируем датафрейм
    dataframe: pd.DataFrame = DataFrameReader(file_path=showcase_file_path).get_file_dataframe()
    TaskOrchestrator.create(name="test", queue_guid='3c787069-8545-4e5d-8263-3b5804646fc0')


if __name__ == '__main__':
    main()
