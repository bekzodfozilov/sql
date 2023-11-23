from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

from keyboards.names import *
from loader import dp
from query_config.config import get_filial, get_city_user
from states.language import Language
from states.menu_state import Menu

filials_list = []


# uz info
@dp.message_handler(text=malumot_uz, state=Language.uz)
async def malumot_handler_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in get_filial(get_city_user(message.from_user.id)):
        markup.insert(i[0])
        filials_list.append(i[0])
    markup.add(back_uz)
    await message.answer('Filialni tanlang:', reply_markup=markup)
    await Menu.step_uz.set()


@dp.message_handler(text=filials_list, state=Menu.step_uz)
async def filial_handler_uz(message: types.Message):
    name = message.text
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in get_filial(get_city_user(message.from_user.id)):
        markup.insert(i[0])
        filials_list.append(i[0])
    markup.add(back_uz)
    for filial in get_filial(get_city_user(message.from_user.id)):
        if filial[0] == name:
            await message.answer_location(latitude=filial[1],
                                          longitude=filial[2],
                                          reply_markup=markup)


# ru info
@dp.message_handler(text=malumot_ru, state=Language.ru)
async def malumot_handler_ru(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in get_filial(get_city_user(message.from_user.id)):
        markup.insert(i[0])
        filials_list.append(i[0])
    markup.add(back_ru)
    await message.answer('Выберите филиал:', reply_markup=markup)
    await Menu.step_ru.set()


@dp.message_handler(text=filials_list, state=Menu.step_ru)
async def filial_handler_ru(message: types.Message):
    name = message.text
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in get_filial(get_city_user(message.from_user.id)):
        markup.insert(i[0])
        filials_list.append(i[0])
    markup.add(back_ru)
    for filial in get_filial(get_city_user(message.from_user.id)):
        if filial[0] == name:
            await message.answer_location(latitude=filial[1],
                                          longitude=filial[2],
                                          reply_markup=markup)


@dp.message_handler(text=malumot_en, state=Language.en)
async def malumot_handler_en(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in get_filial(get_city_user(message.from_user.id)):
        markup.insert(i[0])
        filials_list.append(i[0])
    markup.add(back_en)
    await message.answer('Choose the branch:', reply_markup=markup)
    await Menu.step_en.set()


@dp.message_handler(text=filials_list, state=Menu.step_en)
async def filial_handler_en(message: types.Message):
    name = message.text
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in get_filial(get_city_user(message.from_user.id)):
        markup.insert(i[0])
        filials_list.append(i[0])
    markup.add(back_en)
    for filial in get_filial(get_city_user(message.from_user.id)):
        if filial[0] == name:
            await message.answer_location(latitude=filial[1],
                                          longitude=filial[2],
                                          reply_markup=markup)
