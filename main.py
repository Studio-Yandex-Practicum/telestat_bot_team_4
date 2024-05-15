import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.core.config import settings
from app.core.db import AsyncSessionLocal
from app.middlewares.middleware import DataBaseSession
from app.logs.logger import configure_logging

# Кнопки меню

from app.handlers import base_handlers, handlers
from app.keyboards.set_menu import main_menu


async def main():
    configure_logging('management_bot')
    logging.info('Запуск бота - management_bot.')

    management_bot = Bot(token=settings.management_bot_token)
    report_bot = Bot(token=settings.report_bot_token)
    dp_management = Dispatcher(bot=management_bot)
    dp_management.update.middleware(
        DataBaseSession(async_session=AsyncSessionLocal)
    )
    dp_management.include_router(base_handlers.router)
    dp_management.include_router(handlers.router)

    configure_logging('report_bot')
    logging.info('Запуск бота - report_bot.')

    dp_report = Dispatcher(bot=report_bot)
    dp_report.update.middleware(
        DataBaseSession(async_session=AsyncSessionLocal)
    )
    dp_management.startup.register(main_menu)
    await dp_management.start_polling(management_bot)
    # await dp_report.start_polling(report_bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Ошибка запуска бота')
