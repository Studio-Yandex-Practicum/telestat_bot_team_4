import asyncio

from aiogram import Bot, Dispatcher

from app.core.config import settings


async def main():
    management_bot = Bot(token=settings.management_bot_token)
    report_bot = Bot(token=settings.report_bot_token)
    dp_management = Dispatcher(bot=management_bot)
    dp_report = Dispatcher(bot=report_bot)
    await dp_management.start_polling(management_bot)
    await dp_report.start_polling(report_bot)


if __name__ == '__main__':
    asyncio.run(main())
