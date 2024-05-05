from pydantic_settings import BaseSettings


# Временно для
ADMIN_LIST = {
    123,
}
SUPER_ADMIN = 123


class Settings(BaseSettings):
    management_bot_token: str = "MANAGEMENT_BOT_TOKEN"
    report_bot_token: str = "REPORT_BOT_TOKEN"
    database_url: str = "DATABASE_URL"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
