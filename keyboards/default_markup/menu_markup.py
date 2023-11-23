from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.names import *
menu_markup_uz = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(menu_uz)],
    [KeyboardButton(buyurtmalar_uz),
     KeyboardButton(fikr_bildirish_uz)],
    [KeyboardButton(malumot_uz),
     KeyboardButton(biz_bilan_aloqa_uz)],
    [KeyboardButton(settings_uz)]
])

menu_markup_ru = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(menu_ru)],
    [KeyboardButton(buyurtmalar_ru),
     KeyboardButton(fikr_bildirish_ru)],
    [KeyboardButton(malumot_ru),
     KeyboardButton(biz_bilan_aloqa_ru)],
    [KeyboardButton(settings_ru)]
])

menu_markup_en = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(menu_en)],
    [KeyboardButton(buyurtmalar_en),
     KeyboardButton(fikr_bildirish_en)],
    [KeyboardButton(malumot_en),
     KeyboardButton(biz_bilan_aloqa_en)],
    [KeyboardButton(settings_en)]
])
