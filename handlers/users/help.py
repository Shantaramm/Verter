from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.utils.markdown import hcode, hitalic

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    name = message.from_user.full_name
    text = (f"Привет! Я Вертер, приятно познакомиться {name})\n"
            f"\n"
            f"🌕 Я создан, чтоб помочь тебе!\n"
            f"\n"
            f"🌕 С помощью меня ты можешь сокращать огромные ссылки в маленькие ссылочки!\n"
            f"\n"
            f"🌕 Также, можешь превращать ссылки в QR-коды, и делать с ними все что захочешь!\n"
            f"\n"
            f"🌕 Тебе достаточно ввести одну из команд, вставить ссылку и можешь довольствоваться результатом!\n"
            )
    obratka = "P.S. Обратная связь @Shanty345\n"
    await message.answer(hcode(text))
    await message.answer(hitalic(obratka))
