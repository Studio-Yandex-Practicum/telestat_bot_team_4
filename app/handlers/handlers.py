from aiogram import F, Router
from aiogram.types import CallbackQuery
from app.keyboards.callback_data.callback_data import CallbackData
from app.services.services import collecting_analytics
from app.handlers.text_handlers import HandlersText

router = Router()


@router.callback_query(F.data.in_([CallbackData.CB_ANALYTICS_START]))
async def start_analytics(callback: CallbackQuery):
    await callback.answer(
        text=HandlersText.START_ANALYTICS_COLLECTING,
        show_alert=True,
    )
    data = await callback.bot.get_chat_member(
        callback.message.chat.id, callback.from_user.id
    )
    collecting_analytics(data)
