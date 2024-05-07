from aiogram.types.chat_member_member import ChatMemberMember
from country_list import countries_for_language

countries = dict(countries_for_language('en'))


def collecting_analytics(data: ChatMemberMember):
    user = data.user
    user_data = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'country': countries[user.language_code.upper()],
    }
    return user_data
