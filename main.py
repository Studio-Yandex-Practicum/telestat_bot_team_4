import asyncio

from aiogram import Bot, Dispatcher

from app.core.config import settings
from app.core.db import AsyncSessionLocal, create_db
from app.handlers import base_handlers, handlers
from app.keyboards.set_menu import main_menu
from app.middlewares.middleware import DataBaseSession

# Кнопки меню



async def main():
    management_bot = Bot(token=settings.management_bot_token)
    # report_bot = Bot(token=settings.report_bot_token)
    dp_management = Dispatcher(bot=management_bot)
    dp_management.update.middleware(DataBaseSession(async_session=AsyncSessionLocal))
    dp_management.include_router(base_handlers.router)
    dp_management.include_router(handlers.router)
    # dp_report = Dispatcher(bot=report_bot)
    # dp_report.update.middleware(DataBaseSession(async_session=AsyncSessionLocal))
    dp_management.startup.register(main_menu)
    await create_db()
    await dp_management.start_polling(management_bot)
    # await dp_report.start_polling(report_bot)


if __name__ == '__main__':
    asyncio.run(main())
