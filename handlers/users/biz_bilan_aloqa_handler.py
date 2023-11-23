from aiogram import types

from loader import dp
from states.language import Language
from keyboards.names import *


@dp.message_handler(text=biz_bilan_aloqa_uz, state=Language.uz)
async def biz_bilan_aloqa_uz(message: types.Message):
    await message.answer("""Agar sizda Savollar/Shikoyatlar/Takliflar bo'lsa bizga yozishingiz mumkin: @Street77tech_bot

☎️ Telefon raqam: 71-200-73-73 / 71 200-86-86""")
    await Language.uz.set()


@dp.message_handler(text=biz_bilan_aloqa_ru, state=Language.ru)
async def biz_bilan_aloqa_ru(message: types.Message):
    await message.answer("""Вы можете написать нам, если у вас есть Вопросы/Жалобы/Предложения: @Street77tech_bot

☎️ Телефонный номер: 71-200-73-73 / 71 200-86-86""")
    await Language.ru.set()


@dp.message_handler(text=biz_bilan_aloqa_en, state=Language.en)
async def biz_bilan_aloqa_en(message: types.Message):
    await message.answer("""You can write to us if you have Questions/Complaints/Suggestions: @Street77tech_bot

☎️ Phone number: 71-200-73-73 / 71 200-86-86""")
    await Language.en.set()
