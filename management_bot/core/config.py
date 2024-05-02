from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    management_bot_token: str = 'MANAGEMENT_BOT_TOKEN'
    database_url: str = 'DATABASE_URL'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()
