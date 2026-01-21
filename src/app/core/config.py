from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = "Backend API core"
    VERSION: str = "0.1.0"
    ENVIROMENT: str = Field(default="local")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
