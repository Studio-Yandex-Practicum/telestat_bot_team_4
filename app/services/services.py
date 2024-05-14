from datetime import datetime

import gender_guesser.detector as gender
from country_list import countries_for_language
from pyrogram import Client

from app.core.config import settings

countries = dict(countries_for_language('en'))
d = gender.Detector()

api_id = settings.api_id
api_hash = settings.api_hash
bot_token = settings.management_bot_token


async def chat_members(chat_id):
    app = Client(
        'Имя | Бот',
        api_id=api_id,
        api_hash=api_hash,
        bot_token=bot_token,
        in_memory=True,
    )
    user_data: list[dict] = []
    await app.start()
    async for member in app.get_chat_members(chat_id):
        if member.user.language_code:
            country = countries[member.user.language_code.upper()]
        else:
            country = 'Страна не определена'
        user_data.append(
            {
                'user_id': member.user.id,
                'first_name': member.user.first_name,
                'last_name': member.user.last_name,
                'user_name': member.user.username,
                'country': country,
                'chat_id': chat_id,
                'subscribe_date': datetime.now(),
                'avatar': 'avatar',
                'utm_mark': 'UTM',
                'gender': d.get_gender(member.user.first_name),
                'description': 'description',
            }
        )
    await app.stop()
    return user_data
