from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.keyboards.buttons_text.inline_buttons_text import INLINE_TEXT

analytics_start_button = InlineKeyboardButton(
    text=INLINE_TEXT["analytics_start_button"],
    callback_data="analytics_start_button",
)
keyboard = InlineKeyboardMarkup(inline_keyboard=[[analytics_start_button]])
