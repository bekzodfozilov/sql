from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData

product_cb = CallbackData('product', 'id', 'count', 'action')


def add_markup(id, count, language):
    if language == 'EN':
        add_str = '📥 Add to basket'
    elif language == 'RU':
        add_str = '📥 Добавить в корзину'
    else:
        add_str = '📥 Savatga qoshish'
    global product_cb
    markup = InlineKeyboardMarkup()
    minus_btn = InlineKeyboardButton('➖', callback_data=product_cb.new(id=id, count=count, action='minus'))
    count_btn = InlineKeyboardButton(count, callback_data=product_cb.new(id=id, count=count, action='_'))
    plus_btn = InlineKeyboardButton('➕', callback_data=product_cb.new(id=id, count=count, action='plus'))
    add_btn = InlineKeyboardButton(text=add_str, callback_data=product_cb.new(id=id, count=count, action='add'))
    markup.row(minus_btn, count_btn, plus_btn)
    markup.add(add_btn)
    return markup
