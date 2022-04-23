from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_ROOT_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT:str
    STAGE:str

    class Config:
        env_file = ".env"


def get_settings(): return Settings()