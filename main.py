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
import DB
from Config import TextFiles
from Handlers import AdminCommands

# import background


load_dotenv()
bot = Bot(os.getenv('TEST_TOKEN'))
dp = Dispatcher(bot=bot)

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Начать',
                                                                             callback_data='start_quest')]])

continue_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Продолжить',
                                                                                callback_data='continue_quest')],
                                                          [InlineKeyboardButton(text='Переименоваться',
                                                                                callback_data='start_quest')]])

branch_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ОИТ', callback_data='ОИТ'),
                                                         InlineKeyboardButton(text='ОЭС', callback_data='ОЭС'),
                                                         InlineKeyboardButton(text='ОМЭиКС', callback_data='ОМЭиКС')]])
FINISH_FLAG = False


@dp.message(filters.CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(QuestStates.start_state)
    keyboard = []
    prefix = "Привет!"
    auth = DB.get_auth(message.chat.id)

    if not DB.user_exist(message.from_user.id):
        DB.add_user(message.from_user.id, message.from_user.username)
        keyboard = start_keyboard
    elif "" in auth:
        keyboard = start_keyboard
    else:
        keyboard = continue_keyboard
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
        await message.answer(text=TextFiles.BRANCH_AUTH, reply_markup=branch_keyboard)

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
    user_id = message.chat.id
    await message.answer("не играется")
    # if FINISH_FLAG:
    #     if len(DB.get_quest_stations(user_id)) == len(cards) + 1:
    #         await message.answer(text=TextFiles.FINISH)
    #     else:
    #         await message.answer(text='Квеста завершен! Ответы больше не принимаются)')
    #     return
    #
    # station_name = 'Отправляйся на станцию: '
    # if DB.get_station_status(user_id):
    #     station_name += cards[int(DB.get_quest_stations(user_id)[-2])].question
    #     await bot.send_message(chat_id=user_id, text=station_name)
    #
    #     await state.set_state(QuestStates.station_opened)
    #
    # elif len(DB.get_quest_stations(user_id)) == len(cards) + 1:
    #     await message.answer(text=TextFiles.FINISH)
    #
    # else:
    #     text = station_name + get_station(user_id)
    #     await message.answer(text=text)
    #
    #     await state.set_state(QuestStates.station_opened)


# def get_station(user_id: int) -> str:
# station = random.randint(0, len(cards) - 1)
#
# user_stations = []
# for elem in DB.get_quest_stations(user_id)[:-1]:
#     user_stations.append(int(elem))
#
# while station in user_stations:
#     station = random.randint(0, len(cards) - 1)
#
# DB.save_quest_station(user_id, station)
# DB.open_station(user_id)
#
# return cards[station].question


# @dp.message(QuestStates.station_opened)
# async def check_answer(message: Message, state: FSMContext):
#     user_id = message.chat.id
#     try:
#         print(message.text + ': ' + str(message.chat.id))
#         if message.text.strip().lower() == cards[int(DB.get_quest_stations(user_id)[-2])].answer:
#             await message.answer(text=TextFiles.RIGHT_ANSWER)
#             DB.close_station(user_id)
#             await state.set_state(QuestStates.station_closed)
#             await play_quest(message, state)
#         else:
#             await message.answer(text=TextFiles.WRONG_ANSWER)
#     except:
#         await message.reply(text=TextFiles.TYPE_ERROR_MESSAGE)
#         print(str(message.chat.id) + ' - Шлет что-то странное')


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
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # background.keep_alive()
    asyncio.run(main())
