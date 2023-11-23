from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ovqatlar_uz = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📥 Savat", callback_data='_')],
    [
        InlineKeyboardButton(text="🎉AKSIYA", switch_inline_query_current_chat="🎉AKSIYA"),

        InlineKeyboardButton(text="🥤🌯Summer Set", switch_inline_query_current_chat="🥤🌯Summer Set")],
    [
        InlineKeyboardButton(text="🍕 Pizza", switch_inline_query_current_chat="🍕 Pizza"),

        InlineKeyboardButton(text="🌯 Rollar", switch_inline_query_current_chat="🌯 Rollar")],
    [
        InlineKeyboardButton(text="🍟 Snacks", switch_inline_query_current_chat="🍟 Snacks"),

        InlineKeyboardButton(text="🍔 BURGERS", switch_inline_query_current_chat="🍔 BURGERS")],
    [
        InlineKeyboardButton(text="🥗 Salatlar", switch_inline_query_current_chat="🥗 Salatlar"),

        InlineKeyboardButton(text="🍭 Bolalar uchun", switch_inline_query_current_chat="🍭 Bolalar uchun")],
    [
        InlineKeyboardButton(text="🥤Sovuq ichimliklar", switch_inline_query_current_chat="🥤Sovuq ichimliklar"),

        InlineKeyboardButton(text="🥫Souslar", switch_inline_query_current_chat="🥫Souslar")],
    [
        InlineKeyboardButton(text="🍹Kokteyllar", switch_inline_query_current_chat="🍹Kokteyllar")]

], resize_keyboard=True)

ovqatlar_ru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📥 Корзина", callback_data='_')],
    [
        InlineKeyboardButton(text="🎉AKSIYA", switch_inline_query_current_chat="🎉AKSIYA"),

        InlineKeyboardButton(text="🥤🌯Summer Set", switch_inline_query_current_chat="🥤🌯Summer Set")],
    [
        InlineKeyboardButton(text="🍕 Pizza", switch_inline_query_current_chat="🍕 Pizza"),

        InlineKeyboardButton(text="🌯 Rollar", switch_inline_query_current_chat="🌯 Rollar")],
    [
        InlineKeyboardButton(text="🍟 Snacks", switch_inline_query_current_chat="🍟 Snacks"),

        InlineKeyboardButton(text="🍔 BURGERS", switch_inline_query_current_chat="🍔 BURGERS")],
    [
        InlineKeyboardButton(text="🥗 Salatlar", switch_inline_query_current_chat="🥗 Salatlar"),

        InlineKeyboardButton(text="🍭 Bolalar uchun", switch_inline_query_current_chat="🍭 Bolalar uchun")],
    [
        InlineKeyboardButton(text="🥤Sovuq ichimliklar", switch_inline_query_current_chat="🥤Sovuq ichimliklar"),

        InlineKeyboardButton(text="🥫Souslar", switch_inline_query_current_chat="🥫Souslar")],
    [
        InlineKeyboardButton(text="🍹Kokteyllar", switch_inline_query_current_chat="🍹Kokteyllar")]

], resize_keyboard=True)


def inline_eng(price):
    if price is None:
        price = 0
    ovqatlar_en = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=f"📥 Cart({price})", callback_data='_')],
        [
            InlineKeyboardButton(text="🎉AKSIYA", switch_inline_query_current_chat="🎉AKSIYA"),

            InlineKeyboardButton(text="🥤🌯Summer Set", switch_inline_query_current_chat="🥤🌯Summer Set")],
        [
            InlineKeyboardButton(text="🍕 Pizza", switch_inline_query_current_chat="🍕 Pizza"),

            InlineKeyboardButton(text="🌯 Rollar", switch_inline_query_current_chat="🌯 Rollar")],
        [
            InlineKeyboardButton(text="🍟 Snacks", switch_inline_query_current_chat="🍟 Snacks"),

            InlineKeyboardButton(text="🍔 BURGERS", switch_inline_query_current_chat="🍔 BURGERS")],
        [
            InlineKeyboardButton(text="🥗 Salatlar", switch_inline_query_current_chat="🥗 Salatlar"),

            InlineKeyboardButton(text="🍭 Bolalar uchun", switch_inline_query_current_chat="🍭 Bolalar uchun")],
        [
            InlineKeyboardButton(text="🥤Sovuq ichimliklar", switch_inline_query_current_chat="🥤Sovuq ichimliklar"),

            InlineKeyboardButton(text="🥫Souslar", switch_inline_query_current_chat="🥫Souslar")],
        [
            InlineKeyboardButton(text="🍹Kokteyllar", switch_inline_query_current_chat="🍹Kokteyllar")]

    ], resize_keyboard=True)
    return ovqatlar_en
