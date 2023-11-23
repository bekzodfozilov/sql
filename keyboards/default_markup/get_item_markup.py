from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.names import *

get_markup_uz = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(yetkazib_berish_uz),
     KeyboardButton(olib_ketish_uz)],
    [KeyboardButton(back_uz)]
])

get_markup_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(yetkazib_berish_ru),
     KeyboardButton(olib_ketish_ru)],
    [KeyboardButton(back_ru)]
])

get_markup_en = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(yetkazib_berish_en),
     KeyboardButton(olib_ketish_en)],
    [KeyboardButton(back_en)]
])
