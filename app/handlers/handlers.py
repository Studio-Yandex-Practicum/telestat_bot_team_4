from aiogram import F, Router
from aiogram.types import CallbackQuery
from app.keyboards.callback_data.callback_data import CallbackData
from app.services.services import collecting_analytics
from app.crud.groups import groups_crud

from aiogram.filters.chat_member_updated import (
    ChatMemberUpdatedFilter,
    IS_NOT_MEMBER,
    MEMBER,
    ADMINISTRATOR,
)
from aiogram.types import ChatMemberUpdated


router = Router()
router.my_chat_member.filter(F.chat.type.in_({'group', 'supergroup', 'channel'}))

START_ANALYTICS_COLLECTING = 'Начинаем сбор аналитики.'


@router.callback_query(F.data.in_([CallbackData.CB_ANALYTICS_START]))
async def start_analytics(callback: CallbackQuery):
    await callback.answer(
        text=START_ANALYTICS_COLLECTING,
        show_alert=True,
    )
    data = await callback.bot.get_chat_member(
        callback.message.chat.id, callback.from_user.id
    )
    collecting_analytics(data)


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> (ADMINISTRATOR | MEMBER)
    )
)
async def add_group_to_database(event: ChatMemberUpdated):
    await groups_crud.create(
        group_name=event.chat.title,
        chat_id=event.chat.id,
    )
