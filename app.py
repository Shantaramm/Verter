import logging

from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api import db_link_2

async def on_startup(dispatcher):
    logging.info("Создаем подключение к базе данных")
    await db_link_2.on_startup(dp)
    logging.info("Создаем таблицу пользователей...")
    await db.gino.create_all()
    logging.info("Успешно!")
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

