from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from handlers.users.start_handler import start
from keyboards.default_markup.menu_markup import menu_markup_uz, menu_markup_ru, menu_markup_en
from keyboards.names import *
from loader import dp
from query_config.config import cities, insert_user
from states.language import Language
from states.start_state import Start


# uz registartion
@dp.message_handler(text=back_uz, state=Start.city_uz)
async def back_start_uz(message: types.Message):
    await Start.language.set()
    await start(message)


@dp.message_handler(text=back_uz, state=Start.name_uz)
async def back_language_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_uz)
    await message.answer('Shaharni tanlang:', reply_markup=markup)
    await Start.city_uz.set()


@dp.message_handler(text=back_uz, state=Start.number_uz)
async def back_city_uz(message: types.Message, state: FSMContext):
    await Start.city_uz.set()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_uz)
    await message.answer('Ismingizni yuboring:', reply_markup=markup)
    await Start.name_uz.set()


@dp.message_handler(text='UZ', state=Start.language)
async def start_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_uz)
    await message.answer('Shaharni tanlang:', reply_markup=markup)
    await Start.city_uz.set()


@dp.message_handler(text=cities(), state=Start.city_uz)
async def city_uz(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(
        {'city': city}
    )
    await message.answer(f'{city}ni tanladingiz!')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_uz)
    await message.answer('Ismingizni yuboring:', reply_markup=markup)
    await Start.name_uz.set()


@dp.message_handler(state=Start.city_uz)
async def not_city_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_uz)
    await message.answer('Iltimos boshqa malumot kiritmang❗️', reply_markup=markup)


@dp.message_handler(state=Start.name_uz)
async def name_uz(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer(f'{name} kiritgan ismingiz!')
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact = KeyboardButton('Contact', request_contact=True)
    markup.add(contact)
    markup.add(back_uz)
    await message.answer('Nomeringizni kiriting:', reply_markup=markup)
    await Start.number_uz.set()


@dp.message_handler(state=Start.number_uz, content_types='contact', is_sender_contact=True)
async def number_uz(message: types.Message, state: FSMContext):
    number = message.contact.phone_number
    await state.update_data(
        {'number': number}
    )
    await message.answer('✅ Tayyor')
    async with state.proxy() as data:
        name = data['name']
        city = data['city']
        insert_user(user_id=message.from_user.id, name=name, number=number, language='UZ', city=city)
    await message.answer(f'Bosh menu', reply_markup=menu_markup_uz)
    await Language.uz.set()


@dp.message_handler(state=Start.number_uz)
async def not_number_uz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact = KeyboardButton('Contact', request_contact=True)
    markup.add(contact)
    markup.add(back_uz)
    await message.answer("Iltimos o'z nomeringizni Contact tugmasi orqali jonating❗️", reply_markup=markup)


# ru registartion
@dp.message_handler(text=back_ru, state=Start.city_ru)
async def back_start_ru(message: types.Message):
    await Start.language.set()
    await start(message)


@dp.message_handler(text=back_ru, state=Start.name_ru)
async def back_language_ru(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_ru)
    await message.answer('Выберите город:', reply_markup=markup)
    await Start.city_ru.set()


@dp.message_handler(text=back_ru, state=Start.number_ru)
async def back_city_uz(message: types.Message, state: FSMContext):
    await Start.city_ru.set()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_ru)
    await message.answer('Отправьте вашу имю:', reply_markup=markup)
    await Start.name_ru.set()


@dp.message_handler(text='RU', state=Start.language)
async def start_ru(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_ru)
    await message.answer('Выберите город:', reply_markup=markup)
    await Start.city_ru.set()


@dp.message_handler(text=cities(), state=Start.city_ru)
async def city_ru(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(
        {'city': city}
    )
    await message.answer(f'Вы выбрали {city}!')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_ru)
    await message.answer('Отправьте свою имю:', reply_markup=markup)
    await Start.name_ru.set()


@dp.message_handler(state=Start.city_ru)
async def not_city_ru(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_ru)
    await message.answer('Пожалуйста не введите другую информацию❗️', reply_markup=markup)


@dp.message_handler(state=Start.name_ru)
async def name_ru(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer(f'Вы ввели {name}!')
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact = KeyboardButton('Contact', request_contact=True)
    markup.add(contact)
    markup.add(back_ru)
    await message.answer('Отправьте свой номер:', reply_markup=markup)
    await Start.number_ru.set()


@dp.message_handler(state=Start.number_ru, content_types='contact', is_sender_contact=True)
async def number_ru(message: types.Message, state: FSMContext):
    number = message.contact.phone_number
    await state.update_data(
        {'number': number}
    )
    async with state.proxy() as data:
        name = data['name']
        city = data['city']
        insert_user(user_id=message.from_user.id, name=name, number=number, language='RU', city=city)
    await message.answer('✅ Успешно')
    await message.answer(f'Главный меню', reply_markup=menu_markup_ru)
    await Language.ru.set()


@dp.message_handler(state=Start.number_ru)
async def not_number_ru(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact = KeyboardButton('Contact', request_contact=True)
    markup.add(contact)
    markup.add(back_ru)
    await message.answer("Пожалуйста отправьте свой номер через Contact кнопку❗️", reply_markup=markup)


# en registration
@dp.message_handler(text=back_en, state=Start.city_en)
async def back_start_en(message: types.Message):
    await Start.language.set()
    await start(message)


@dp.message_handler(text=back_en, state=Start.name_en)
async def back_language_en(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_en)
    await message.answer('Choose city:', reply_markup=markup)
    await Start.city_en.set()


@dp.message_handler(text=back_en, state=Start.number_en)
async def back_city_en(message: types.Message, state: FSMContext):
    await Start.city_en.set()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_en)
    await message.answer('Send me your name:', reply_markup=markup)
    await Start.name_en.set()


@dp.message_handler(text='EN', state=Start.language)
async def start_en(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_en)
    await message.answer('Choose city:', reply_markup=markup)
    await Start.city_en.set()


@dp.message_handler(text=cities(), state=Start.city_en)
async def city_en(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(
        {'city': city}
    )
    await message.answer(f'You chose {city}!')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(f'{message.from_user.first_name}')
    markup.add(back_en)
    await message.answer('Send me your name :', reply_markup=markup)
    await Start.name_en.set()


@dp.message_handler(state=Start.city_en)
async def not_city_en(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    for i in cities():
        markup.insert(i)
    markup.add(back_en)
    await message.answer('Please do not enter other informations❗️', reply_markup=markup)


@dp.message_handler(state=Start.name_en)
async def name_en(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer(f'You entered {name}!')
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact = KeyboardButton('Contact', request_contact=True)
    markup.add(contact)
    markup.add(back_en)
    await message.answer('Send your phone number:', reply_markup=markup)
    await Start.number_en.set()


@dp.message_handler(state=Start.number_en, content_types='contact', is_sender_contact=True)
async def number_en(message: types.Message, state: FSMContext):
    number = message.contact.phone_number
    await state.update_data(
        {'number': number}
    )
    await message.answer('✅ ✅ Done')
    async with state.proxy() as data:
        name = data['name']
        city = data['city']
        insert_user(user_id=message.from_user.id, name=name, number=number, language='EN', city=city)
    await message.answer(f'Main menu', reply_markup=menu_markup_en)
    await Language.en.set()


@dp.message_handler(state=Start.number_en)
async def not_number_en(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact = KeyboardButton('Contact', request_contact=True)
    markup.add(contact)
    markup.add(back_en)
    await message.answer("Please send me your number with Contact button❗️", reply_markup=markup)


@dp.message_handler(state=Start.language)
async def language(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('UZ', 'RU', 'EN')
    await message.answer('❗️ ❗ ❗️\nFaqat UZ RU EN\nТолько UZ RU EN\nOnly UZ RU EN', reply_markup=markup)
