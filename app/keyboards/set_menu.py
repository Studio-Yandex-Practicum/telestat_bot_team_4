from aiogram import Bot
from aiogram.types import BotCommand
from app.keyboards.buttons_text.menu_text import MENU_BUTTONS_TEXT


async def main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in MENU_BUTTONS_TEXT.items()
    ]
    await bot.set_my_commands(main_menu_commands)
