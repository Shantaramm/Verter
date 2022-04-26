from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncpg.exceptions

from keyboards.default import menu
from loader import dp
from utils.db_api import commands as db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    await db.add_user(id=message.from_user.id, name=name)
    await message.answer(f"🔴 Добро пожаловать, {name}!\n"
                         f"\n"
                         f"🔴 Я робот Вертер!\n"
                         f"\n"
                         f"🔴 С помощью меня ты можешь сократить ссылку ✂️\n\n🔴 И даже превратить ее в QR-код 🖼!\n")
    await message.answer("Чтобы ты хотел?", reply_markup=menu)
#5023845448:AAH4L5MwF7YOA6IWSh6vXylVkEvGC_2qJr8
#2041780885:AAE73UutUiUin6jx-rV_Ah_OXMT2y4Bmt9E