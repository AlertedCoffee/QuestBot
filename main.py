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
bot = Bot(os.getenv('TEST_TOKEN'))
dp = Dispatcher(bot=bot)

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Начать',
                                                                             callback_data='start_quest')]])

cards = StationsFactory().get_cards()


@dp.message(filters.CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(QuestStates.start_state)
    if not DB.user_exist(message.from_user.id):
        DB.add_user(message.from_user.id, message.from_user.username)
    await message.answer(f"{TextFiles.GREETING}",
                         reply_markup=start_keyboard)


@dp.message(filters.Command('alert'))
async def alert_users(message: Message) -> None:
    if message.from_user.id not in [542687360, 890780591]:
        return
    try:
        users = DB.get_user_list()
        for user in users:
            try:
                await bot.send_message(text=message.html_text.replace('/alert', ''), chat_id=user[0], parse_mode='HTML')
            except:
                pass
    except:
        pass


@dp.message(filters.Command('finish'))
async def finish_quest(message: Message) -> None:
    if message.from_user.id not in [542687360, 890780591]:
        return
    global FINISH_FLAG
    FINISH_FLAG = True


@dp.message(filters.Command('finish_cancel'))
async def finish_quest_cancel(message: Message) -> None:
    if message.from_user.id not in [542687360, 890780591]:
        return
    global FINISH_FLAG
    FINISH_FLAG = False


@dp.callback_query(lambda c: c.data == 'start_quest')
async def start_quest(call: types.CallbackQuery, state: FSMContext) -> None:
    await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=None)

    await play_quest(call.message, state)

FINISH_FLAG = False


async def play_quest(message: Message, state: FSMContext) -> None:
    user_id = message.chat.id
    if not FINISH_FLAG:
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
    else:
        if len(DB.get_quest_stations(user_id)) == len(cards) + 1:
            await message.answer(text=TextFiles.FINISH)
        else:
            await message.answer(text='Квеста завершен! Ответы больше не принимаются)')


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
    user_id = message.chat.id
    try:
        print(message.text + ': ' + str(message.chat.id))
        if message.text.strip().lower() == cards[int(DB.get_quest_stations(user_id)[-2])].answer:
            await message.answer(text=TextFiles.RIGHT_ANSWER)
            DB.close_station(user_id)
            await state.set_state(QuestStates.station_closed)
            await play_quest(message, state)
        else:
            await message.answer(text=TextFiles.WRONG_ANSWER)
    except:
        await message.reply(text="Ты отправляешь что-то странное. Я принимаю только текст!\n"
                                 "А возможно у тебя не настроен username в telegram")
        print(str(message.chat.id) + ' - Шлет что-то странное')


@dp.message()
async def check_answer(message: Message, state: FSMContext):
    user_id = message.chat.id
    try:
        print(message.text + ': ' + str(message.chat.id))
    except:
        pass

    await bot.send_message(chat_id=user_id, text=TextFiles.ERROR_MESSAGE)


async def main() -> None:
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # background.keep_alive()
    asyncio.run(main())



