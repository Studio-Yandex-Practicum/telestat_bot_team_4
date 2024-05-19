from aiogram.fsm.state import State, StatesGroup


class GetUserID(StatesGroup):
    user_id = State()
