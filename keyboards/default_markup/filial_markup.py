from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.names import *
yetkazib_berish_markup_uz = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text=location_uz, request_location=True)],
    [KeyboardButton(text=my_adress_uz)],
    [KeyboardButton(text=back_uz)]
])

yetkazib_berish_markup_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text=location_ru, request_location=True)],
    [KeyboardButton(text=my_adress_ru)],
    [KeyboardButton(text=back_ru)]
])

yetkazib_berish_markup_en = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text=location_en, request_location=True)],
    [KeyboardButton(text=my_adress_en)],
    [KeyboardButton(text=back_en)]
])
