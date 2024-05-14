import asyncio

from aiogram import Bot, Dispatcher

from middlewares.middleware import DataBaseSession

from app.core.config import settings
from core.db import AsyncSessionLocal

# Кнопки меню

from app.handlers import base_handlers, handlers
from app.keyboards.set_menu import main_menu


async def main():
    management_bot = Bot(token=settings.management_bot_token)
    # report_bot = Bot(token=settings.report_bot_token)
    dp_management = Dispatcher(bot=management_bot)
    dp_management.update.middleware(
        DataBaseSession(async_session=AsyncSessionLocal)
    )
    dp_management.include_router(base_handlers.router)
    dp_management.include_router(handlers.router)
    # dp_report = Dispatcher(bot=report_bot)
    dp_management.startup.register(main_menu)
    await dp_management.start_polling(management_bot)
    # await dp_report.start_polling(report_bot)


if __name__ == '__main__':
    asyncio.run(main())
