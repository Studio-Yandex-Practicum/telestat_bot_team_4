from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ButtonsText:
    ANALYTICS_START = "Начать сбор аналитики"
    MANAGING_ADMIN = "Управление адмиистраторами"
    MANAGIN_ANALYTICS = "Аналитика"
    ADD_ADMIN = "Добавить админа"
    DELETE_ADMIN = "Удалить админа"


def get_on_start_kb():
    """Запуск сбора аналитики."""
    button_start_analitics = KeyboardButton(text=ButtonsText.ANALYTICS_START)
    buttons_row = [button_start_analitics]
    markup = ReplyKeyboardMarkup(
        keyboard=[buttons_row], resize_keyboard=True, is_persistent=True
    )

    return markup


def get_on_admin_kb():
    """Управление админкой."""
    button_managing_admin = KeyboardButton(text=ButtonsText.MANAGING_ADMIN)
    button_managing_analytics = KeyboardButton(text=ButtonsText.MANAGIN_ANALYTICS)
    buttons_row = [button_managing_admin, button_managing_analytics]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    return markup


def get_on_admin_manage_kb() -> ReplyKeyboardMarkup:
    """Добавить, удалить админа."""
    builder = ReplyKeyboardBuilder()
    builder.button(text=ButtonsText.ADD_ADMIN)
    builder.button(text=ButtonsText.DELETE_ADMIN)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
