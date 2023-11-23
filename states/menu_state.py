from aiogram.dispatcher.filters.state import State, StatesGroup


class Menu(StatesGroup):
    step_uz = State()
    step1_uz = State()
    step2_uz = State()

    step_ru = State()
    step1_ru = State()
    step2_ru = State()

    step_en = State()
    step1_en = State()
    step2_en = State()
