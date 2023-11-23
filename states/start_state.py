from aiogram.dispatcher.filters.state import State, StatesGroup


class Start(StatesGroup):
    language = State()

    city_uz = State()
    name_uz = State()
    number_uz = State()

    city_ru = State()
    name_ru = State()
    number_ru = State()

    city_en = State()
    name_en = State()
    number_en = State()
