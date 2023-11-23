from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline_markup.items_inline import add_markup, product_cb
from handlers.users.menu_handler import filial_handler_en
from loader import dp, db


@dp.callback_query_handler(product_cb.filter(action='add'), state="*")
async def Cart(query: types.CallbackQuery, state: FSMContext, callback_data: dict):
    count = callback_data['count']
    item_id = callback_data['id']
    user_id = query.from_user.id
    print(count)
    sql = 'insert into cart(count, item_id, user_id) values (?, ?, ?)'
    db.execute(sql=sql, parameters=(int(count), int(item_id), str(user_id)), commit=True)
    await query.answer()
    await query.message.delete()
    print(query.message)
    await filial_handler_en(query.message)
