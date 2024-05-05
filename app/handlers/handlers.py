from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.in_(["analytics_start_button"]))
async def start_analytics(callback: CallbackQuery):
    await callback.message.answer("Начинаем сбор аналитики")
