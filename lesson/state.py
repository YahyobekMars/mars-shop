from aiogram.dispatcher.filters.state import StatesGroup, State


class TestCreateState(StatesGroup):
    question = State()
    answer_1 = State()
    answer_2 = State()
    answer_3 = State()
    answer_4 = State()
    right_answer = State()   