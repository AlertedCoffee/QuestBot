import asyncio
import os
from dotenv import load_dotenv
import random

from aiogram import Bot, Dispatcher, types, filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Model.StationsFactory import StationsFactory
from Model.QuestStates import QuestStates
import DB
from Config import TextFiles
# import background


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Начать',
                                                                             callback_data='start_quest')]])

cards = StationsFactory().get_cards()


@dp.message(filters.CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    try:
        await state.set_state(QuestStates.start_state)
        if not DB.user_exist(message.from_user.id):
            DB.add_user(message.from_user.id, message.from_user.username)
        await message.answer(f"{TextFiles.GREETING}",
                             reply_markup=start_keyboard)
        # else:
        #     await message.answer(text=f'А тебя я уже знаю, {message.from_user.username}!')
        #     await play_quest(message, state)
    except Exception as ex:
        await bot.send_message(chat_id=542687360, text=str(ex) + 'id: ' + str(message.from_user.id))


@dp.callback_query(lambda c: c.data == 'start_quest')
async def start_quest(call: types.CallbackQuery, state: FSMContext) -> None:
    await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=None)

    # await call.message.answer(text='Ну погнали')
    await play_quest(call.message, state)


async def play_quest(message: Message, state: FSMContext) -> None:
    user_id = message.chat.id
    station_name = 'Отправляйся на станцию: '
    if DB.get_station_status(user_id):
        station_name += cards[int(DB.get_quest_stations(user_id)[-2])].station_name
        await bot.send_message(chat_id=user_id, text=station_name)

        await state.set_state(QuestStates.station_opened)

    elif len(DB.get_quest_stations(user_id)) == len(cards) + 1:
        await message.answer(text=TextFiles.FINISH)

    else:
        text = station_name + get_station(user_id)
        await message.answer(text=text)

        await state.set_state(QuestStates.station_opened)


def get_station(user_id: int) -> str:
    station = random.randint(0, len(cards) - 1)

    user_stations = []
    for elem in DB.get_quest_stations(user_id)[:-1]:
        user_stations.append(int(elem))

    while station in user_stations:
        station = random.randint(0, len(cards) - 1)

    DB.save_quest_station(user_id, station)
    DB.open_station(user_id)

    return cards[station].station_name


@dp.message(QuestStates.station_opened)
async def check_answer(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text.strip().lower() == cards[int(DB.get_quest_stations(user_id)[-2])].answer:
        await message.answer(text=TextFiles.RIGHT_ANSWER)
        DB.close_station(user_id)
        await state.set_state(QuestStates.station_closed)
        await play_quest(message, state)
    else:
        await message.answer(text=TextFiles.WRONG_ANSWER)


async def main() -> None:
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # background.keep_alive()
    asyncio.run(main())



