from aiogram import Dispatcher, types

from loader import dp


async def set_default_commands(disp: Dispatcher):
    await disp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("info", "Информация о боте")
    ])


@dp.message_handler(commands='info')
async def info(message: types.Message):
    await message.answer("Это самый удобный бот который есть. Тут есть все что желаете")
