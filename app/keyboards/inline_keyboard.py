from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.keyboards.buttons_text.inline_buttons_text import InlineButtonsText
from app.keyboards.callback_data.callback_data import CallbackData


def analytics_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=InlineButtonsText.START_ANALYTICS,
        callback_data=CallbackData.CB_ANALYTICS_START,
    )
    return builder.as_markup()


kb_analytics = analytics_keyboard()
