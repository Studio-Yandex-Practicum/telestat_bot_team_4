import asyncio

from aiogram import Bot, Dispatcher

from management_bot.core import management_bot_settings
from report_bot.core import report_bot_settings


async def main():
    management_bot = Bot(token=management_bot_settings.management_bot_token)
    report_bot = Bot(token=report_bot_settings.report_bot_token)
    dp_management = Dispatcher(bot=management_bot)
    dp_report = Dispatcher(bot=report_bot)
    await dp_management.start_polling(management_bot)
    await dp_report.start_polling(report_bot)


if __name__ == '__main__':
    asyncio.run(main())
