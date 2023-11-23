from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


from keyboards.default_markup.filial_markup import yetkazib_berish_markup_en, \
    yetkazib_berish_markup_ru, yetkazib_berish_markup_uz
from keyboards.default_markup.get_item_markup import get_markup_uz, get_markup_en, get_markup_ru
from keyboards.default_markup.menu_markup import menu_markup_uz, menu_markup_ru, menu_markup_en
from keyboards.inline_markup.inline_markup import ovqatlar_uz, ovqatlar_ru
from keyboards.names import *
from loader import dp, db
from query_config.config import get_filial, get_city_user
from states.language import Language
from states.menu_state import Menu
from keyboards.inline_markup.inline_markup import inline_eng

filials_list = []


# uz MENU
@dp.message_handler(text=menu_uz, state=Language.uz)
async def menu_handler_uz(message: types.Message):
    await message.answer("Buyurtmani o'zingiz olib keting yoki Yetkazib berishni tanlang", reply_markup=get_markup_uz)
    await Menu.step_uz.set()


@dp.message_handler(text=olib_ketish_uz, state=Menu.step_uz)
async def olib_ketish_uz(message: types.Message):
    filial_markup_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
        [KeyboardButton(text=location_uz, request_location=True)]])
    for i in get_filial(get_city_user(message.from_user.id)):
        filial_markup_uz.insert(i[0])
        filials_list.append(i[0])
    filial_markup_uz.add(back_uz)
    await message.answer("""Qayerdasiz 👀?
Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni aniqlaymiz""", reply_markup=filial_markup_uz)
    await Menu.step1_uz.set()


@dp.message_handler(text=yetkazib_berish_uz, state=Menu.step_uz)
async def yetkazib_berish_uz(message: types.Message):
    await message.answer("""Buyurtmangizni qayerga yetkazib berish kerak 🚙?
Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni va yetkazib berish xarajatlarini aniqlaymiz 💵""",
                         reply_markup=yetkazib_berish_markup_uz)
    await Menu.step1_uz.set()


@dp.message_handler(text=filials_list, state=Menu.step1_uz)
async def filial_handler_uz(message: types.Message):
    name = message.text
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(main_menu_uz)
    await message.answer(f'Tanlagan filialingiz {name}', reply_markup=markup)
    await message.answer('Nimadan boshlaymiz', reply_markup=ovqatlar_uz)
    await Menu.step1_uz.set()


@dp.message_handler(text=main_menu_uz, state=Menu.step1_uz)
async def glav_menu_uz(message: types.Message):
    await message.answer('Bosh menu', reply_markup=menu_markup_uz)
    await Language.uz.set()


@dp.message_handler(text=back_uz, state=Menu.step_uz)
async def ortga_step_uz(message: types.Message, state: FSMContext):
    await glav_menu_uz(message)


@dp.message_handler(text=back_uz, state=Menu.step1_uz)
async def ortga_step1_uz(message: types.Message):
    await menu_handler_uz(message)
    await Menu.step_uz.set()


# ru MENU
@dp.message_handler(text=menu_ru, state=Language.ru)
async def menu_handler_ru(message: types.Message):
    await message.answer("Заберите свой заказ самостоятельно 🙋‍♂️ или выберите доставку 🚙", reply_markup=get_markup_ru)
    await Menu.step_ru.set()


@dp.message_handler(text=olib_ketish_ru, state=Menu.step_ru)
async def olib_ketish_ru(message: types.Message):
    filial_markup_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
        [KeyboardButton(text=location_ru, request_location=True)]])
    for i in get_filial(get_city_user(message.from_user.id)):
        filial_markup_ru.insert(i[0])
        filials_list.append(i[0])
    filial_markup_ru.add(back_ru)
    await message.answer("""Где Вы находитесь 👀?
Если Вы отправите локацию 📍, мы определим ближайший к Вам филиал""", reply_markup=filial_markup_ru)
    await Menu.step1_ru.set()


@dp.message_handler(text=yetkazib_berish_ru, state=Menu.step_ru)
async def yetkazib_berish_ru(message: types.Message):
    await message.answer("""Куда нужно доставить Ваш заказ 🚙?
Если Вы отправите локацию 📍, мы определим ближайший к Вам филиал и стоимость доставки 💵.""",
                         reply_markup=yetkazib_berish_markup_ru)
    await Menu.step1_ru.set()


@dp.message_handler(text=filials_list, state=Menu.step1_ru)
async def filial_handler_ru(message: types.Message):
    name = message.text
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(main_menu_ru)
    await message.answer(f'Выбранный филиал {name}', reply_markup=markup)
    await message.answer('С чего начнем', reply_markup=ovqatlar_ru)
    await Menu.step1_ru.set()


@dp.message_handler(text=main_menu_ru, state=Menu.step1_ru)
async def glav_menu_ru(message: types.Message):
    await message.answer('Главный меню', reply_markup=menu_markup_ru)
    await Language.ru.set()


@dp.message_handler(text=back_ru, state=Menu.step_ru)
async def ortga_step_ru(message: types.Message):
    await glav_menu_ru(message)


@dp.message_handler(text=back_ru, state=Menu.step1_ru)
async def ortga_step1_ru(message: types.Message):
    await menu_handler_ru(message)
    await Menu.step_ru.set()


# en MENU
@dp.message_handler(text=menu_en, state=Language.en)
async def menu_handler_en(message: types.Message):
    await message.answer("Pick up your order yourself 🙋‍♂️ or select delivery 🚙", reply_markup=get_markup_en)
    await Menu.step_en.set()


@dp.message_handler(text=olib_ketish_en, state=Menu.step_en)
async def olib_ketish_en(message: types.Message):
    filial_markup_en = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
        [KeyboardButton(text=location_en, request_location=True)]])
    for i in get_filial(get_city_user(message.from_user.id)):
        filial_markup_en.insert(i[0])
        filials_list.append(i[0])
    filial_markup_en.add(back_en)
    await message.answer("""Where are you located 👀?
If you send a location 📍, we will determine the closest branch to you""", reply_markup=filial_markup_en)
    await Menu.step1_en.set()


@dp.message_handler(text=yetkazib_berish_en, state=Menu.step_en)
async def yetkazib_berish_en(message: types.Message):
    await message.answer("""Where do you need to deliver your order 🚙?
If you send a location 📍, we will determine the closest branch to you and the delivery cost 💵.""",
                         reply_markup=yetkazib_berish_markup_en)
    await Menu.step1_en.set()


@dp.message_handler(text=main_menu_en, state=Menu.step1_en)
async def glav_menu_en(message: types.Message):
    await message.answer('Main menu', reply_markup=menu_markup_en)
    await Language.en.set()


@dp.message_handler(text=back_en, state=Menu.step_en)
async def ortga_step_en(message: types.Message):
    await glav_menu_en(message)


@dp.message_handler(text=back_en, state=Menu.step1_en)
async def ortga_step1_en(message: types.Message):
    await menu_handler_en(message)
    await Menu.step_en.set()


@dp.message_handler(text=filials_list, state=Menu.step1_en)
async def filial_handler_en(message: types.Message):
    sql = '''select sum(count*i.price) from  cart
join items i on i.id = cart.item_id
where user_id = ?'''

    price = db.execute(sql=sql, parameters=(str(message.chat.id),), fetchone=True)[0]
    name = message.text
    markup = inline_eng(price)
    await message.answer(f'Branch selected {name}')
    await message.answer('Where do we start?', reply_markup=markup)
    await Menu.step1_en.set()

