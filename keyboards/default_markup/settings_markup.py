from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.names import *

setting_markup_uz = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text=change_name_uz),
         KeyboardButton(text=change_number_uz)],
        [KeyboardButton(text=change_city_uz),
         KeyboardButton(text=change_lang_uz)],
        [KeyboardButton(text=back_uz)]
    ])

setting_markup_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text=change_name_ru),
         KeyboardButton(text=change_number_ru)],
        [KeyboardButton(text=change_city_ru),
         KeyboardButton(text=change_lang_ru)],
        [KeyboardButton(text=back_ru)]
    ])

setting_markup_en = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text=change_name_en),
         KeyboardButton(text=change_number_en)],
        [KeyboardButton(text=change_city_en),
         KeyboardButton(text=change_lang_en)],
        [KeyboardButton(text=back_en)]
    ])
