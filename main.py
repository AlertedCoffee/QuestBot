import asyncio
import os
from dotenv import load_dotenv
import DB

from aiogram import Bot, Dispatcher, types, filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Начать', callback_data='start_quest')]])


@dp.message(filters.CommandStart())
async def command_start_handler(message: Message) -> None:
    try:
        if not DB.user_exist(message.from_user.id):
            DB.add_user(message.from_user.id, message.from_user.username)
            await message.answer(f"{message.from_user.username}, Привет! Это бот квеста. Желаешь начать?",
                                 reply_markup=start_keyboard)
        else:
            await message.answer(text='а тебя я уже знаю')
    except Exception as ex:
        await bot.send_message(chat_id=542687360, text=str(ex) + 'id: ' + str(message.from_user.id))


@dp.callback_query(lambda c: c.data == 'start_quest')
async def start_quest(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    await call.message.answer(text='Ну погнали')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())



