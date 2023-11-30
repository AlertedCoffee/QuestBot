import asyncio
import datetime
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
from Handlers import MainHandler
from keyboards import MainKeyboards


# import background


load_dotenv()
bot = Bot(os.getenv('MASTER_TOKEN'))
dp = Dispatcher(bot=bot)


FINISH_FLAG = False

cards = []


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


@dp.message(filters.Command('alert'))
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


@dp.message(filters.Command('alert_to'))
async def alert_users(message: Message) -> None:
    if message.from_user.id not in [542687360]:
        return

    try:
        text = message.html_text.replace('/alert_to', '')
        text = text.split('##')
        test = '##'.join(text[1:])
        await bot.send_message(text=test, chat_id=text[0].strip(), parse_mode='HTML')
    except Exception as ex:
        await bot.send_message(text=str(ex), chat_id=542687360)


@dp.message(filters.Command('leaders'))
async def alert_users(message: Message) -> None:
    admin = 542687360
    if message.from_user.id != admin:
        return

    table = [DB.get_oi_leaders_list(),
             DB.get_oe_leaders_list(),
             DB.get_om_leaders_list(),
             DB.get_oo_leaders_list()]

    text = ""
    for branch in table:
        if branch:
            text += "\n\n" + branch[0][3] + "\n"
            for person in branch:
                text += f"<code>{person[0]}</code> @{person[1]} {person[2]}\nбаллы: {person[4]} время: {person[5]} \n\n"

    await bot.send_message(chat_id=admin, text=text, parse_mode='HTML')


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
        keyboard = MainKeyboards.continue_rename_keyboard
        prefix = f"Рад приветствовать тебя снова, {auth[0]} из {auth[1]}!"
    await message.answer(f"{prefix + TextFiles.GREETING}",
                         reply_markup=keyboard, parse_mode='HTML')


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


@dp.callback_query(lambda c: c.data in ['ОЭиС', 'ОМЭиКС', 'ОИТ', 'ООПНиПТ'])
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
        await state.set_state(QuestStates.quest_finished)
        return
    elif FINISH_FLAG:
        await message.answer(text=TextFiles.QUEST_CLOSED)
        await state.set_state(QuestStates.quest_finished)
        return

    await message.answer(card.question)
    await state.set_state(QuestStates.station_opened)


def get_current_station(message: Message, state: FSMContext) -> StationCard:
    user_id = message.chat.id

    users_stations = [DB.get_first_group_stations(user_id),
                      DB.get_second_group_stations(user_id)]
                      # DB.get_third_group_stations(user_id)]

    if len(users_stations[0]) + len(users_stations[1]) == 10:
        return StationCard('', '', 0, 0)  # complete

    for group_id, station in enumerate(users_stations):
        if len(station) <= 5:
            if len(station) == 0:
                return get_random_station(user_id, group_id)

            elif len(station) == 5 and station[-1][1] == 0:
                pass

            elif station[-1][1] == 1:
                return cards[group_id][station[-1][0]]
            else:
                return get_random_station(user_id, group_id)


def get_random_station(user_id: int, group: int) -> StationCard:
    while True:
        try:
            station = random.randint(0, len(cards[group]) - 1)
            DB.open_station(user_id, station, group)
            return cards[group][station]
        except:
            pass


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

    try:
        print(message.text + ': ' + str(message.chat.id))
        DB.close_station(user_id, card.id, card.group)

        if card.check_answer(message.text):
            DB.add_score(user_id, card.group + 1)

        DB.add_time(user_id, DB.get_time_delt(user_id, card.id, card.group))

        await state.set_state(QuestStates.station_closed)
        await message.answer(text=TextFiles.RIGHT_ANSWER, reply_markup=MainKeyboards.continue_keyboard)

    except:
        await message.reply(text=TextFiles.TYPE_ERROR_MESSAGE)
        print(str(message.chat.id) + ' - Шлет что-то странное')


@dp.message()
async def check_answer(message: Message, state: FSMContext):
    user_id = message.chat.id
    try:
        print(message.text + ': ' + str(message.chat.id))
    except:
        pass
    s = await state.get_state()

    if s is None:
        await bot.send_message(chat_id=user_id, text=TextFiles.BOT_RESTART)
    elif s in [QuestStates.start_state, QuestStates.branch_auth, QuestStates.station_closed]:
        await message.answer(TextFiles.INVALID_TEXT_ON_BUTTON)
    else:
        await message.answer(TextFiles.INVALID_TEXT)


async def main() -> None:
    # dp.include_router(MainHandler.router)
    # MainHandler.bot_init(bot)

    global cards
    cards = [StationsFactory().get_cards_first_group(),
             StationsFactory().get_cards_second_group()]
             # StationsFactory().get_cards_third_group()]


    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
