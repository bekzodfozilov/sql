from aiogram import types

from keyboards.default_markup.fikr_bildirish_markup import *
from loader import dp
from states.language import Language
from states.menu_state import Menu
from keyboards.names import *


# uz FIKR
@dp.message_handler(text=fikr_bildirish_uz, state=Language.uz)
async def fikr_handler_uz(message: types.Message):
    await message.answer("""✅ Street 77ni tanlaganingiz uchun rahmat.
Agar Siz bizning hizmatlarimiz sifatini yaxshilashga yordam bersangiz, bundan benihoya xursand bo'lamiz.
Buning uchun 5 ballik tizim asosida baholang""", reply_markup=fikr_markup_uz)
    await Menu.step_uz.set()


# ru FIKR
@dp.message_handler(text=fikr_bildirish_ru, state=Language.ru)
async def fikr_handler_ru(message: types.Message):
    await message.answer("""✅ Контроль сервиса доставки Street 77.
Мы благодарим за сделанный выбор и будем рады, если Вы оцените нашу работу по 5 бальной шкале""", reply_markup=fikr_markup_ru)
    await Menu.step_ru.set()


# en FIKR
@dp.message_handler(text=fikr_bildirish_en, state=Language.en)
async def fikr_handler_en(message: types.Message):
    await message.answer("""✅ Monitoring the Street 77 delivery service.
We thank you for your choice and we will be glad if you rate our work on a 5-point scale""", reply_markup=fikr_markup_en)
    await Menu.step_en.set()
