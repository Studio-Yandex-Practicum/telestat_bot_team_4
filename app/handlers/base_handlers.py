from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart
from app.keyboards.inline_keyboard import kb_analytics
from app.core.config import ADMIN_LIST
from app.handlers.text_handlers import BaseHandlersText

router = Router()


@router.message(CommandStart(), ~F.from_user.id.in_(ADMIN_LIST))
async def start_not_admin(message: types.Message):
    await message.answer(
        text=BaseHandlersText.NOT_ADMIN,
    )


@router.message(CommandStart(), F.from_user.id.in_(ADMIN_LIST))
async def start_admin(message: types.Message):
    await message.answer(
        text=BaseHandlersText.ANALYTICS_COLLECTING,
        reply_markup=kb_analytics,
    )
