from aiogram.dispatcher.filters.state import State, StatesGroup


class Update(StatesGroup):
    language_uz = State()
    city_uz = State()
    number_uz = State()
    name_uz = State()

    language_ru = State()
    city_ru = State()
    number_ru = State()
    name_ru = State()

    language_en = State()
    city_en = State()
    number_en = State()
    name_en = State()
