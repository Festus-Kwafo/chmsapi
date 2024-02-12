from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Literal


class Settings(BaseSettings):
    # Env Config
    ENVIRONMENT: Literal["dev", "prod"]

    # Env MySQL
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str

    DB_ECHO: bool = False

    # Env Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DATABASE: int

    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    # FastAPI
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'FastAPI'
    VERSION: str = '0.0.1'
    DESCRIPTION: str = 'Church Management System API'
    DOCS_URL: str | None = f'{API_V1_STR}/docs'
    REDOCS_URL: str | None = f'{API_V1_STR}/redocs'
    OPENAPI_URL: str | None = f'{API_V1_STR}/openapi'

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # Logs
    LOG_STDOUT_FILENAME: str = 'chmsapi_access.log'
    LOG_STDERR_FILENAME: str = 'chmsapi_error.log'

    # Demo mode
    # Only GET, OPTIONS requests are allowed
    DEMO_MODE: bool = False
    DEMO_MODE_EXCLUDE: set[tuple[str, str]] = {
        ('POST', f'{API_V1_STR}/auth/login'),
        ('POST', f'{API_V1_STR}/auth/logout'),
        ('GET', f'{API_V1_STR}/auth/captcha'),
    }

    # Middleware
    MIDDLEWARE_CORS: bool = True
    MIDDLEWARE_ACCESS: bool = True

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
