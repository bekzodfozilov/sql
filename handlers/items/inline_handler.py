from aiogram import types

from keyboards.names import *
from loader import dp
from query_config.config import db, get_kategory
from states.menu_state import Menu


def items(kategory):
    list_item = []
    try:
        fetchall = db.execute(f"""select * from items where kategory = '{kategory}'""", fetchall=True)
        for i in fetchall:
            list_item.append(i)
        return list_item
    except Exception as err:
        print(err)


# UZ
@dp.inline_handler(text=get_kategory(), state=Menu.step1_uz)
async def inline(inline: types.InlineQuery):
    print('OKKKKKKK')
    msg = []
    for i in items(inline.query):
        msg.append((
            types.InlineQueryResultArticle(
                id=str(i[0]),
                title=i[2],
                input_message_content=types.InputMessageContent(
                    message_text=i[2]
                ),
                thumb_url=i[5],
                description=i[3]
            )

        ))
    msg.append((
        types.InlineQueryResultArticle(
            id=str('back'),
            title=back_uz,
            input_message_content=types.InputMessageContent(
                message_text="⬅️ Kategoriyaga"
            ),
            thumb_url='https://cdn.pixabay.com/photo/2017/06/20/14/55/icon-2423347_1280.png',
            description="Возвращает назад в категорию"

        )

    ))
    await Menu.step2_uz.set()
    await inline.answer(results=msg)


@dp.message_handler(text='⬅️ Kategoriyaga', state=Menu.step1_uz)
async def nazad(message: types.Message):
    await message.delete()


# RU
@dp.inline_handler(text=get_kategory(), state=Menu.step1_ru)
async def inline(inline: types.InlineQuery):
    msg = []
    for i in items(inline.query):
        msg.append((
            types.InlineQueryResultArticle(
                id=str(i[0]),
                title=i[2],
                input_message_content=types.InputMessageContent(
                    message_text=i[2]
                ),
                thumb_url=i[5],
                description=i[3]
            )

        ))
    msg.append((
        types.InlineQueryResultArticle(
            id=str('back'),
            title=back_ru,
            input_message_content=types.InputMessageContent(
                message_text="⬅️ Назад в категорию"
            ),
            thumb_url='https://cdn.pixabay.com/photo/2017/06/20/14/55/icon-2423347_1280.png',
            description="Возвращает назад в категорию"

        )

    ))
    await Menu.step2_ru.set()
    await inline.answer(results=msg)


@dp.message_handler(text='⬅️ Назад в категорию', state=Menu.step1_ru)
async def nazad(message: types.Message):
    await message.delete()


# EN
@dp.inline_handler(text=get_kategory(), state=Menu.step1_en)
async def inline(inline: types.InlineQuery):
    msg = []
    for i in items(inline.query):
        msg.append((
            types.InlineQueryResultArticle(
                id=str(i[0]),
                title=i[2],
                input_message_content=types.InputMessageContent(
                    message_text=i[2]
                ),
                thumb_url=i[5],
                description=i[3]
            )

        ))
    msg.append((
        types.InlineQueryResultArticle(
            id=str('back'),
            title=back_en,
            input_message_content=types.InputMessageContent(
                message_text="⬅️ Back to items"
            ),
            thumb_url='https://cdn.pixabay.com/photo/2017/06/20/14/55/icon-2423347_1280.png',
            description="Возвращает назад в категорию"

        )

    ))
    await Menu.step2_en.set()
    await inline.answer(results=msg)


@dp.message_handler(text='⬅️ Back to items', state=Menu.step1_en)
async def nazad(message: types.Message):
    await message.delete()
