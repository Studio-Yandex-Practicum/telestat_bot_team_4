from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest

router = Router()


@router.errors_handler(exception=TelegramBadRequest)
async def error_admin_is_superuser(
    update: types.Update, exception: TelegramBadRequest
):
    print('Нельзя удалить суперюзера!')
    return True
