from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

from keyboards.inline_markup.inline_markup import ovqatlar_uz
from loader import dp, bot
from keyboards.inline_markup.items_inline import add_markup, product_cb
from query_config.config import get_item, update_plus_count, update_minus_count, db, users
from states.menu_state import Menu
from keyboards.names import *


def item():
    name = []
    try:
        fetchall = db.execute("""select name from items""", fetchall=True)
        for i in fetchall:
            for j in i:
                name.append(j)
        return name
    except Exception as err:
        print(err)


@dp.callback_query_handler(product_cb.filter(action='_'), state=Menu.step2_uz)
@dp.callback_query_handler(product_cb.filter(action='minus'), state=Menu.step2_uz)
@dp.callback_query_handler(product_cb.filter(action='plus'), state=Menu.step2_uz)
async def add(callback: types.CallbackQuery, callback_data: dict):
    action = callback_data['action']
    item_id = callback_data['id']
    count = callback_data['count']
    count = int(count)
    if action == 'plus':
        count += 1
        update_plus_count(callback.from_user.id)
        await bot.edit_message_reply_markup(callback.message.chat.id,
                                            callback.message.message_id,
                                            inline_message_id=callback.inline_message_id,
                                            reply_markup=add_markup(item_id, count, 'UZ'))
        await callback.answer()

    elif action == 'minus':
        if count == 1:
            await callback.answer('1 Minimum')
        else:
            count -= 1
            update_minus_count(callback.from_user.id)
            await bot.edit_message_reply_markup(callback.message.chat.id,
                                                callback.message.message_id,
                                                inline_message_id=callback.inline_message_id,
                                                reply_markup=add_markup(item_id, count, 'UZ'))
            await callback.answer()
    else:
        await callback.answer(f'Soni {count}')


@dp.message_handler(text=back_uz, state=Menu.step2_uz)
async def back_step2_uz(message: types.Message):
    await message.answer('Menu', reply_markup=ovqatlar_uz)
    await Menu.step1_uz.set()


# RU
@dp.callback_query_handler(product_cb.filter(action='_'), state=Menu.step2_ru)
@dp.callback_query_handler(product_cb.filter(action='minus'), state=Menu.step2_ru)
@dp.callback_query_handler(product_cb.filter(action='plus'), state=Menu.step2_ru)
async def add(callback: types.CallbackQuery, callback_data: dict):
    action = callback_data['action']
    item_id = callback_data['id']
    count = callback_data['count']
    count = int(count)
    if action == 'plus':
        count += 1
        update_plus_count(callback.from_user.id)
        await bot.edit_message_reply_markup(callback.message.chat.id,
                                            callback.message.message_id,
                                            inline_message_id=callback.inline_message_id,
                                            reply_markup=add_markup(item_id, count, 'RU'))
        await callback.answer()

    elif action == 'minus':
        if count == 1:
            await callback.answer('Минимум до 1')
        else:
            count -= 1
            update_minus_count(callback.from_user.id)
            await bot.edit_message_reply_markup(callback.message.chat.id,
                                                callback.message.message_id,
                                                inline_message_id=callback.inline_message_id,
                                                reply_markup=add_markup(item_id, count, 'RU'))
            await callback.answer()
    else:
        await callback.answer(f'Количество {count}')


# EN
@dp.callback_query_handler(product_cb.filter(action='_'), state=Menu.step2_en)
@dp.callback_query_handler(product_cb.filter(action='minus'), state=Menu.step2_en)
@dp.callback_query_handler(product_cb.filter(action='plus'), state=Menu.step2_en)
async def add(callback: types.CallbackQuery, callback_data: dict):
    action = callback_data['action']
    item_id = callback_data['id']
    count = callback_data['count']
    count = int(count)
    if action == 'plus':
        count += 1
        update_plus_count(callback.from_user.id)
        await bot.edit_message_reply_markup(callback.message.chat.id,
                                            callback.message.message_id,
                                            inline_message_id=callback.inline_message_id,
                                            reply_markup=add_markup(item_id, count, 'EN'))
        await callback.answer()

    elif action == 'minus':
        if count == 1:
            await callback.answer('Minimum 1')
        else:
            count -= 1
            update_minus_count(callback.from_user.id)
            await bot.edit_message_reply_markup(callback.message.chat.id,
                                                callback.message.message_id,
                                                inline_message_id=callback.inline_message_id,
                                                reply_markup=add_markup(item_id, count, 'EN'))
            await callback.answer()
    else:
        await callback.answer(f'Quantity {count}')


# UZ RU EN
@dp.message_handler(text=item(), state='*')
async def my_basket(message: types.Message):
    await message.delete()
    item_name = message.text
    it = get_item(item_name)
    item_id = it[0]
    count = 1
    language = str()
    for i in users():
        if i[1] == str(message.from_user.id):
            language = i[5]
    if language == 'UZ':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(back_uz)
        await message.answer('Modifikator tanlang:', reply_markup=markup)
        await message.answer_photo(photo=it[5],
                                   caption=f"{it[2]}\n\n{it[3]}\n\n{it[4]} sum",
                                   reply_markup=add_markup(item_id, count, 'UZ'))
    elif language == 'RU':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(back_ru)
        await message.answer('Выберите действие:', reply_markup=markup)
        await message.answer_photo(photo=it[5],
                                   caption=f"{it[2]}\n\n{it[3]}\n\n{it[4]} сум",
                                   reply_markup=add_markup(item_id, count, 'RU'))
    elif language == 'EN':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(back_en)
        await message.answer('Choose a modifier:', reply_markup=markup)
        await message.answer_photo(photo=it[5],
                                   caption=f"{it[2]}\n\n{it[3]}\n\n{it[4]} sum",
                                   reply_markup=add_markup(item_id, count, 'EN'))
