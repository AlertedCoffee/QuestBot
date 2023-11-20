from aiogram import Router, filters, Bot
from aiogram.types import Message

import DB


router = Router()
bot: Bot


def bot_init(botik: Bot):
    global bot
    bot = botik


@router.message(filters.Command('alert'))
async def alert_users(message: Message) -> None:
    if message.from_user.id not in [542687360]:
        return
    try:
        users = DB.get_users_list()
        for user in users:
            try:

                await bot.send_message(text=message.html_text.replace('/alert', ''), chat_id=user[0], parse_mode='HTML')
            except:
                pass
    except:
        pass