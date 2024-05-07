from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart
from app.keyboards.inline_keyboard import kb_analytics
from app.core.config import ADMIN_LIST


router = Router()

NOT_ADMIN = 'К сожалению, у вас нет прав доступа.'
ANALYTICS_COLLECTING = 'Начать сбор аналитики.'


@router.message(CommandStart(), ~F.from_user.id.in_(ADMIN_LIST))
async def start_not_admin(message: types.Message):
    await message.answer(
        text=NOT_ADMIN,
    )


@router.message(CommandStart(), F.from_user.id.in_(ADMIN_LIST))
async def start_admin(message: types.Message):
    await message.answer(
        text=ANALYTICS_COLLECTING,
        reply_markup=kb_analytics,
    )
