from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def admin_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [
            KeyboardButton(text='Добавить администратора'),
            KeyboardButton(text='Удалить администратора'),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Что вы собираетесь сделать?'
    )
    return keyboard.as_markup(resize_keyboard=True)
