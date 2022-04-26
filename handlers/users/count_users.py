import logging

from aiogram import types

from data.config import ADMINS
from loader import dp
from utils.db_api import commands as db


@dp.message_handler(commands="count_users")
async def qr_link(message: types.Message):
    count = await db.count_users()
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, f"Колличество пользователей базы данных - {count} человек")
        except Exception as err:
            logging.exception(err)
