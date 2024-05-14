from aiogram import Router, types
from aiogram.filters import CommandStart

from app.filters.filters import IsAdmin
from app.keyboards.inline_keyboard import kb_analytics

router = Router()

NOT_ADMIN = 'К сожалению, у вас нет прав доступа.'
ANALYTICS_COLLECTING = 'Начать сбор аналитики.'


@router.message(CommandStart(), ~IsAdmin())
async def start_not_admin(message: types.Message):
    await message.answer(
        text=NOT_ADMIN,
    )


@router.message(CommandStart(), IsAdmin())
async def start_admin(message: types.Message):
    await message.answer(
        text=ANALYTICS_COLLECTING,
        reply_markup=kb_analytics,
    )
