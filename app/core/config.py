from pydantic_settings import BaseSettings


# Временно для
ADMIN_LIST = {
    146708975,
}
SUPER_ADMIN = 146708975


class Settings(BaseSettings):
    management_bot_token: str = "MANAGEMENT_BOT_TOKEN"
    report_bot_token: str = "REPORT_BOT_TOKEN"
    database_url: str = "DATABASE_URL"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
