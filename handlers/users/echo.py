from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

from keyboards.default_markup.menu_markup import menu_markup_uz, menu_markup_ru, menu_markup_en
from loader import dp
from query_config.config import users, create_tables
from states.language import Language
from states.start_state import Start


@dp.message_handler(state='*')
async def echo(message: types.Message):
    language = str()
    create_tables()
    if str(message.from_user.id) in [i[1] for i in users()]:
        for i in users():
            if i[1] == str(message.from_user.id):
                language = i[5]
        if str(language) == 'UZ':
            await Language.uz.set()
            await message.answer(f'Bosh menu', reply_markup=menu_markup_uz)
        elif str(language) == 'RU':
            await Language.ru.set()
            await message.answer(f'Главный меню', reply_markup=menu_markup_ru)
        elif str(language) == 'EN':
            await Language.en.set()
            await message.answer(f'Main menu', reply_markup=menu_markup_en)
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('UZ', 'RU', 'EN')
        await message.answer(f'Tilni tanlang\nВыберите язык\nChoose language', reply_markup=markup)
        await Start.language.set()
