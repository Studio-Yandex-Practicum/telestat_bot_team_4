from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart
from app.keyboards.inline_keyboard import kb_analytics
from app.core.config import ADMIN_LIST, SUPER_ADMIN

router = Router()


@router.message(CommandStart(), ~F.from_user.id.in_(ADMIN_LIST))
async def start_not_admin(message: types.Message):
    await message.answer(
        text="К сожалению, у вас нет прав доступа.",
    )
    # Предложение слать суперадмину такое сообщение
    # Сценарий использования: Суперадмин шлет ссылку на бот
    # Человеку которого планирует добавиь администратором
    # Тот жмет кнопку старт, суперадмин получает сообщение
    # с именем и id пользователя  и заносит его в базу
    # Как вариант к сообщению можно прикрутить кнопки добавить\отклонить
    # По нажатию на кнопку добавить, id пользователя добавляется в базу.
    # Ну либо в печку все, лишние телодвижения нам не нужны =)
    await message.bot.send_message(
        SUPER_ADMIN,
        text=(
            f"Пользователь: {message.from_user.username}, "
            f"id: {message.from_user.id} пытался получить доступ к боту."
        ),
    )


@router.message(CommandStart(), F.from_user.id.in_(ADMIN_LIST))
async def start_admin(message: types.Message):
    await message.answer(
        text="Начать сбор аналитики.",
        reply_markup=kb_analytics,
    )
