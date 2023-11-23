from aiogram import Router, filters, Bot
from aiogram.types import Message

import DB


router = Router()
bot: Bot


def bot_init(botik: Bot):
    global bot
    bot = botik