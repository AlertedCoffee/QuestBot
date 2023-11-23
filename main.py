import asyncio
import os
from dotenv import load_dotenv
import random

from aiogram import Bot, Dispatcher, types, filters, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Model.StationsFactory import StationsFactory
from Model.QuestStates import QuestStates
from Model.StationModel import StationCard
import DB
from Config import TextFiles
from Handlers import AdminCommands
from keyboards import MainKeyboards


# import background


load_dotenv()
bot = Bot(os.getenv('TEST_TOKEN'))
dp = Dispatcher(bot=bot)


FINISH_FLAG = False

cards = []


@dp.message(filters.CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(QuestStates.start_state)
    keyboard = []
    prefix = "Привет!"
    auth = DB.get_auth(message.chat.id)

    if not DB.user_exist(message.from_user.id):
        DB.add_user(message.from_user.id, message.from_user.username)
        keyboard = MainKeyboards.start_keyboard
    elif "" in auth:
        keyboard = MainKeyboards.start_keyboard
    else:
        keyboard = MainKeyboards.continue_keyboard
        prefix = f"Рад приветствовать тебя снова, {auth[0]} из {auth[1]}!"
    await message.answer(f"{prefix + TextFiles.GREETING}",
                         reply_markup=keyboard)


async def drop_inline(call: types.CallbackQuery) -> None:
    await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=None)


@dp.callback_query(lambda c: c.data == 'start_quest')
async def start_quest(call: types.CallbackQuery, state: FSMContext) -> None:
    await drop_inline(call)

    await call.message.answer(TextFiles.FIO_AUTH)
    await state.set_state(QuestStates.fio_auth)


@dp.callback_query(lambda c: c.data == 'continue_quest')
async def start_quest(call: types.CallbackQuery, state: FSMContext) -> None:
    await drop_inline(call)
    await play_quest(call.message, state)


@dp.message(QuestStates.fio_auth)
async def fio_auth(message: Message, state: FSMContext) -> None:
    user_id = message.chat.id
    try:
        print(message.text + ': ' + str(message.chat.id))
        DB.set_user_fio(user_id, message.text)
        await message.answer("Записано!")

        await state.set_state(QuestStates.branch_auth)
        await message.answer(text=TextFiles.BRANCH_AUTH, reply_markup=MainKeyboards.branch_keyboard)

    except:
        await message.reply(text=TextFiles.TYPE_ERROR_MESSAGE)
        print(str(message.chat.id) + ' - Шлет что-то странное')


@dp.callback_query(lambda c: c.data in ['ОЭС', 'ОМЭиКС', 'ОИТ'])
async def branch_auth(call: types.CallbackQuery, state: FSMContext) -> None:
    await drop_inline(call)
    if await state.get_state() == QuestStates.branch_auth:
        try:
            DB.set_user_branch(call.message.chat.id, call.data)
            await play_quest(call.message, state)
        except:
            pass


async def play_quest(message: Message, state: FSMContext) -> None:
    card = get_current_station(message, state)

    if card.answer == '':
        await message.answer(text=TextFiles.FINISH)
        return
    elif FINISH_FLAG:
        await message.answer(text=TextFiles.QUEST_CLOSED)
        return

    await message.answer(card.question)
    await state.set_state(QuestStates.station_opened)


def get_current_station(message: Message, state: FSMContext) -> StationCard:
    user_id = message.chat.id

    users_stations = [DB.get_first_group_stations(user_id),
                      DB.get_second_group_stations(user_id),
                      DB.get_third_group_stations(user_id)]

    if len(users_stations[0]) + len(users_stations[1]) + len(users_stations[2]) == 15:
        return StationCard('', '', 0, 0)  # complete

    for group_id, station in enumerate(users_stations):
        if len(station) <= 5:
            if len(station) == 0:
                return get_random_station(user_id, group_id, station)

            elif len(station) == 5 and station[-1][1] == 0:
                pass

            elif station[-1][1] == 1:
                return cards[group_id][station[-1][0]]
            else:
                return get_random_station(user_id, group_id, station)


def get_random_station(user_id: int, group: int, user_stations: []) -> StationCard:
    station = random.randint(0, len(cards[group]) - 1)

    try:
        while station_existing_check(station, user_stations):
            station = random.randint(0, len(cards[group]) - 1)
    except:
        pass

    DB.open_station(user_id, station, group)

    return cards[group][station]


def station_existing_check(station: int, user_stations) -> bool:
    for i in user_stations:
        if station == i[0]:
            return True
        else:
            return False


@dp.message(QuestStates.station_opened)
async def check_answer(message: Message, state: FSMContext):
    user_id = message.chat.id

    card = get_current_station(message, state)

    DB.close_station(user_id, card.id, card.group)

    await state.set_state(QuestStates.station_closed)

    await play_quest(message, state)

    # try:
    #     print(message.text + ': ' + str(message.chat.id))
    #     if message.text.strip().lower() == cards[int(DB.get_quest_stations(user_id)[-2])].answer:
    #         await message.answer(text=TextFiles.RIGHT_ANSWER)
    #         DB.close_station(user_id)
    #         await state.set_state(QuestStates.station_closed)
    #         await play_quest(message, state)
    #     else:
    #         await message.answer(text=TextFiles.WRONG_ANSWER)
    # except:
    #     await message.reply(text=TextFiles.TYPE_ERROR_MESSAGE)
    #     print(str(message.chat.id) + ' - Шлет что-то странное')


@dp.message()
async def check_answer(message: Message, state: FSMContext):
    user_id = message.chat.id
    try:
        print(message.text + ': ' + str(message.chat.id))
    except:
        pass
    if await state.get_state() not in [QuestStates.branch_auth, QuestStates.start_state]:
        await bot.send_message(chat_id=user_id, text=TextFiles.ERROR_MESSAGE)
    else:
        await message.answer(TextFiles.INVALID_TEXT)


@dp.message(filters.Command('finish'))
async def finish_quest(message: Message) -> None:
    if message.from_user.id not in [542687360]:
        return
    global FINISH_FLAG
    FINISH_FLAG = True


@dp.message(filters.Command('finish_cancel'))
async def finish_quest_cancel(message: Message) -> None:
    if message.from_user.id not in [542687360]:
        return
    global FINISH_FLAG
    FINISH_FLAG = False


async def main() -> None:
    dp.include_router(AdminCommands.router)
    AdminCommands.bot_init(bot)

    global cards
    cards = [StationsFactory().get_cards_first_group(),
             StationsFactory().get_cards_second_group(),
             StationsFactory().get_cards_third_group()]

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # background.keep_alive()
    asyncio.run(main())
