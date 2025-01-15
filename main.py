import config.env_loader  # Необходимо для загрузки всех переменных окружения

from src.get_table_info.ossdep_requests import DataDownloader


def main() -> None:
    DataDownloader.download_data(params={'table': 'cons_dm.wfm_ppr_outsherpa'},
                                 output_file_name='cons_dm.wfm_ppr_outsherpa.json.gzip')


if __name__ == '__main__':
    main()
