from app.crud.groups import groups_crud
from app.crud.user import user_crud

from aiogram import F, Router
from aiogram.types import CallbackQuery
from app.keyboards.callback_data.callback_data import CallbackData
from aiogram.filters.chat_member_updated import (
    ChatMemberUpdatedFilter,
    IS_NOT_MEMBER,
    MEMBER,
    ADMINISTRATOR,
)
from aiogram.types import ChatMemberUpdated
from app.services.services import chat_members
from sqlalchemy.ext.asyncio import AsyncSession


router = Router()
router.my_chat_member.filter(F.chat.type.in_({'group', 'supergroup', 'channel'}))

START_ANALYTICS_COLLECTING = 'Начинаем сбор аналитики.'


@router.callback_query(F.data.in_([CallbackData.CB_ANALYTICS_START]))
# Здесь нужно выбирать чат в котором будет собираться аналитика.
# Так же сопоставлять пользоватлей из базы с полученым списком
# Если есть в базе но нет в списке, считать его отписавшимся и заполнять unsubscribe_date


async def start_analytics(
    callback: CallbackQuery, session: AsyncSession, chat_id: str = '-0'
) -> None:
    chat_id = callback.message.chat.id
    await callback.answer(
        text=START_ANALYTICS_COLLECTING,
        show_alert=True,
    )
    group_user_list = await chat_members(chat_id)
    db_user = await user_crud.get_all(session=session)
    db_user_id_list = [user.user_id for user in db_user]
    for user in group_user_list:
        if user['user_id'] not in db_user_id_list:
            # тут получается длякаждого юзера открываем сессию, добаляем данные
            # делаем комит, по уму комит надо делать после добавления всех данных
            await user_crud.create(session=session, **user)


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> (ADMINISTRATOR | MEMBER)
    )
)
async def add_group_to_database(
    event: ChatMemberUpdated, session: AsyncSession
) -> None:
    group = await groups_crud.get(session=session, group_id=event.chat.id)
    if not group:
        await groups_crud.create(
            session=session,
            group_name=event.chat.title,
            group_id=event.chat.id,
        )
