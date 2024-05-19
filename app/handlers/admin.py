from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from crud.admin import CRUDAdmin
from keyboards.admin import admin_keyboard
from .states import GetUserID

router = Router()


@router.message(Command('admin'))
async def add_or_delete_admin(message: Message):
    await message.answer(
        'Выберите необходимое действие',
        reply_markup=admin_keyboard(),
    )


@router.message(F.text.lower() == 'добавить администратора')
async def get_user_id_to_add_admin(message: Message, state: FSMContext):
    await message.answer(
        'Введите ID пользователя, которого хотите сделать администратором',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(GetUserID.user_id)


@router.message(F.text.lower() == 'удалить администратора')
async def get_admin_id_to_remove(message: Message, state: FSMContext):
    await message.answer(
        'Введите ID пользователя, которого хотите удалить из администраторов',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(GetUserID.user_id)


@router.message(
    GetUserID.user_id,
    F.text
)
async def add_admin(message: Message):
    from_user_admin_obj = CRUDAdmin.get(id=message.from_user.id)
    if from_user_admin_obj.is_superuser:
        CRUDAdmin.create(id=message.text)
        await message.answer(
            text='Администратор добавлен!',
            reply_markup=admin_keyboard()
        )
    else:
        await message.answer(
            text='У вас недостаточно прав!',
            reply_markup=admin_keyboard()
        )


@router.message(
    GetUserID.user_id,
    F.text
)
async def remove_admin(message: Message):
    from_user_admin_obj = CRUDAdmin.get(id=message.from_user.id)
    removing_admin_obj = CRUDAdmin.get(id=message.text)
    if not from_user_admin_obj.is_superuser:
        await message.answer(
            text='У вас недостаточно прав!',
            reply_markup=admin_keyboard()
        )
    elif not removing_admin_obj:
        await message.answer(
            text='Такого администратора не существует или ID некорректный!',
            reply_markup=admin_keyboard()
        )
    else:
        CRUDAdmin.remove(id=message.text)
        await message.answer(
            text='Администратор удален!',
            reply_markup=admin_keyboard()
        )
