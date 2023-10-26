from aiogram.fsm.state import State, StatesGroup


class QuestStates(StatesGroup):
    station_opened = State()
    station_closed = State()
    start_state = State()

