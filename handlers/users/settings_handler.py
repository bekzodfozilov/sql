from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default_markup.settings_markup import setting_markup_uz, setting_markup_ru, setting_markup_en
from keyboards.names import *
from loader import dp
from query_config.config import update_language, cities, update_city, users
from states.language import Language
from states.menu_state import Menu
from states.update_state import Update


# setting_uz
@dp.message_handler(text=settings_uz, state=Language.uz)
async def sozlama_hand_uz(message: types.Message):
    await message.answer('Sizning malumotlaringiz:')
    for i in users():
        if i[1] == str(message.from_user.id):
            await message.answer(f"Ism - <i><b>{i[2]}</b></i> | Nomer - <i><b>{i[3]}</b></i> | Shahar - <i><b>{i[4]}</b></i>")
    await message.answer('Harakat tanlang:', reply_markup=setting_markup_uz)
    await Menu.step_uz.set()


@dp.message_handler(text=change_lang_uz, state=Menu.step_uz)
async def change_language_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('UZ', 'RU', 'EN')
    await message.answer('Tilni tanlang', reply_markup=markup)
    await Update.language_uz.set()


@dp.message_handler(text=['UZ', 'RU', 'EN'], state=Update.language_uz)
async def change_uz(message: types.Message):
    language = message.text
    await Menu.step_uz.set()
    update_language(message.from_user.id, language)
    if language == 'RU':
        await sozlama_hand_ru(message)
    if language == 'UZ':
        await sozlama_hand_uz(message)
    if language == 'EN':
        await sozlama_hand_en(message)


@dp.message_handler(text=change_city_uz, state=Menu.step_uz)
async def change_city_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    await message.answer('Shaharni jonating:', reply_markup=markup)
    await Update.city_uz.set()


@dp.message_handler(text=cities(), state=Update.city_uz)
async def change_city_uz(message: types.Message):
    city = message.text
    await message.answer(f"Shahar {city}ga ozgardi", reply_markup=setting_markup_uz)
    await Menu.step_uz.set()
    update_city(message.from_user.id, city)


@dp.message_handler(text=change_name_uz, state=Menu.step_uz)
async def change_name_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_uz)
    await message.answer('Yangi ismni jonating:', reply_markup=markup)
    await Update.name_uz.set()


@dp.message_handler(state=Update.name_uz)
async def update_name_uz(message: types.Message):
    name = message.text
    await message.answer(f'Ism {name}ga ozgardi', reply_markup=setting_markup_uz)
    await Menu.step_uz.set()


# setting ru
@dp.message_handler(text=settings_ru, state=Language.ru)
async def sozlama_hand_ru(message: types.Message):
    await message.answer('Ваши данные:')
    for i in users():
        if i[1] == str(message.from_user.id):
            await message.answer(f"Имя <i><b>{i[2]}</b></i> | Номер <i><b>{i[3]}</b></i> | Город <i><b>{i[4]}</b></i>")
    await message.answer('Выберите действие:', reply_markup=setting_markup_ru)
    await Menu.step_ru.set()


@dp.message_handler(text=change_lang_ru, state=Menu.step_ru)
async def change_language_ru(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('UZ', 'RU', 'EN')
    await message.answer('Выберите язык', reply_markup=markup)
    await Update.language_ru.set()


@dp.message_handler(text=['UZ', 'RU', 'EN'], state=Update.language_ru)
async def change_uz(message: types.Message):
    language = message.text
    await Menu.step_ru.set()
    update_language(message.from_user.id, language)
    if language == 'RU':
        await sozlama_hand_ru(message)
    if language == 'UZ':
        await sozlama_hand_uz(message)
    if language == 'EN':
        await sozlama_hand_en(message)


@dp.message_handler(text=change_city_ru, state=Menu.step_ru)
async def change_city_ru(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    await message.answer('Отправьте город:', reply_markup=markup)
    await Update.city_ru.set()


@dp.message_handler(text=cities(), state=Update.city_ru)
async def change_city_ru(message: types.Message):
    city = message.text
    await message.answer(f"""Город поменян на {city}""", reply_markup=setting_markup_ru)
    await Menu.step_ru.set()
    update_city(message.from_user.id, city)


@dp.message_handler(text=change_name_ru, state=Menu.step_ru)
async def change_name_ru(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_ru)
    await message.answer('Отправьте мне новую имю:', reply_markup=markup)
    await Update.name_ru.set()


@dp.message_handler(state=Update.name_ru)
async def update_name_ru(message: types.Message):
    name = message.text
    await message.answer(f'Имя поменян на {name}', reply_markup=setting_markup_ru)
    await Menu.step_ru.set()


# setting en
@dp.message_handler(text=settings_en, state=Language.en)
async def sozlama_hand_en(message: types.Message):
    await message.answer('Your information:')
    for i in users():
        if i[1] == str(message.from_user.id):
            await message.answer(f"Name <i><b>{i[2]}</b></i> | Number <i><b>{i[3]}</b></i> | City <i><b>{i[4]}</b></i>")
    await message.answer('Choose an action:', reply_markup=setting_markup_en)
    await Menu.step_en.set()


@dp.message_handler(text=change_lang_en, state=Menu.step_en)
async def change_language_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('UZ', 'RU', 'EN')
    await message.answer('Choose language', reply_markup=markup)
    await Update.language_en.set()


@dp.message_handler(text=['UZ', 'RU', 'EN'], state=Update.language_en)
async def change_uz(message: types.Message):
    language = message.text
    await Menu.step_en.set()
    update_language(message.from_user.id, language)
    if language == 'RU':
        await sozlama_hand_ru(message)
    if language == 'UZ':
        await sozlama_hand_uz(message)
    if language == 'EN':
        await sozlama_hand_en(message)


@dp.message_handler(text=change_city_en, state=Menu.step_en)
async def change_city_en(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    await message.answer('Send me city:', reply_markup=markup)
    await Update.city_en.set()


@dp.message_handler(text=cities(), state=Update.city_en)
async def change_city_en(message: types.Message):
    city = message.text
    await message.answer(f"City changed to {city}", reply_markup=setting_markup_en)
    await Menu.step_en.set()
    update_city(message.from_user.id, city)


@dp.message_handler(text=change_name_en, state=Menu.step_en)
async def change_name_en(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_en)
    await message.answer('Send me new name:', reply_markup=markup)
    await Update.name_en.set()


@dp.message_handler(state=Update.name_en)
async def update_name_en(message: types.Message):
    name = message.text
    await message.answer(f'Name changed to {name}', reply_markup=setting_markup_en)
    await Menu.step_en.set()
