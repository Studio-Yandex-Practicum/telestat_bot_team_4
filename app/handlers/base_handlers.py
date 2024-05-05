from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart
from app.keyboards.inline_keyboard import keyboard

router = Router()

ADMIN_LIST = {
    111,
}  # Получим из БД


@router.message(CommandStart(), ~F.from_user.id.in_(ADMIN_LIST))
async def start_not_admin(message: types.Message):
    await message.answer(
        text="К сожалению, у вас нет прав доступа.",
    )


@router.message(CommandStart(), F.from_user.id.in_(ADMIN_LIST))
async def start_admin(message: types.Message):
    await message.answer(
        text="Начать сбор аналитики.",
        reply_markup=keyboard,
    )
