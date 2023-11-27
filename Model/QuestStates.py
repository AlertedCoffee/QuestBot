from aiogram.fsm.state import State, StatesGroup


class QuestStates(StatesGroup):
    station_opened = State()
    station_closed = State()
    start_state = State()
    fio_auth = State()
    branch_auth = State()
    quest_finished = State()

