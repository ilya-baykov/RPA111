from pydantic_settings import BaseSettings, SettingsConfigDict

from config.constants.paths import DB_ENV_PATH
from config.logger import logger


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        db_url = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        logger.info(db_url)
        return db_url

    @classmethod
    def configure(cls, env_file: str):
        cls.model_config = SettingsConfigDict(env_file=env_file)


Settings.configure(DB_ENV_PATH)
db_report_settings = Settings()
