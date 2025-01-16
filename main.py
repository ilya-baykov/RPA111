import pandas as pd

from src.get_table_info.ossdep_requests import DataDownloader
from src.get_table_info.dataframe_reader import DataFrameReader


def main() -> None:
    file_path = DataDownloader.download_data(params={'table': 'cons_dm.wfm_ppr_outsherpa'},
                                             output_file_name='showcase.txt')
    data_frame: pd.DataFrame = DataFrameReader(file_path=file_path).get_file_dataframe()
    print(data_frame)


if __name__ == '__main__':
    main()
