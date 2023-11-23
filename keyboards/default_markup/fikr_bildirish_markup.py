from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.names import *

fikr_markup_uz = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
    [KeyboardButton(text='Hammasi yoqdi ♥️')],
    [KeyboardButton(text='Yaxshi ⭐️⭐️⭐️⭐️')],
    [KeyboardButton(text='Yoqmadi ⭐️⭐️⭐️')],
    [KeyboardButton(text='Yomon ⭐️⭐️')],
    [KeyboardButton(text='Juda yomon 👎🏻')],
    [KeyboardButton(text=back_uz)]
])

fikr_markup_ru = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
    [KeyboardButton(text='😊Все понравилось, на 5 ❤️')],
    [KeyboardButton(text='☺️Нормально, на 4 ⭐️⭐️⭐️⭐️')],
    [KeyboardButton(text='😐Удовлетворительно, на 3 ⭐️⭐️⭐️️⭐️')],
    [KeyboardButton(text='☹️Не понравилось, на 2 ⭐️⭐️')],
    [KeyboardButton(text='😤Хочу пожаловаться 👎🏻')],
    [KeyboardButton(text=back_ru)]
])

fikr_markup_en = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
    [KeyboardButton(text='😊Liked everything 5 ❤️')],
    [KeyboardButton(text='☺️Normal, at 4 ⭐️⭐️⭐️⭐️')],
    [KeyboardButton(text='😐Satisfactory, by 3 ⭐️⭐️⭐️️⭐️')],
    [KeyboardButton(text='☹️Dont like it, 2 ⭐️⭐️')],
    [KeyboardButton(text='😤I want to complain 👎🏻')],
    [KeyboardButton(text=back_en)]
])
