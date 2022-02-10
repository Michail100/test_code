import logging
import asyncio
from aiogram import Bot, types,executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from config import get_fromenv
from settings import bot, dp, create_db
from config import WEBAPP_HOST, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_PORT, WEBHOOK_HOST
from database.database_handlers import insert_into_table
from handlers.handlers import register_base_handlers
from aiogram.types.bot_command import BotCommand
from settings import cursor


dp.middleware.setup(LoggingMiddleware())


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/get_data',description='Получить данные'),
        BotCommand(command='/insert_data', description='Добавить данные'),
        BotCommand(command='/update_data', description='Редактировать данные'),
        BotCommand(command='/delete_data', description='Очистить таблицу'),
        BotCommand(command='/drop_id_key', description='Сбросить id')
    ]
    await bot.set_my_commands(commands)


async def on_startup(dp):
    await asyncio.sleep(10)
    await set_commands(bot)
    await bot.set_webhook(WEBHOOK_URL)
    await create_db()
    register_base_handlers(dp)


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    #await bot.delete_webhook()

    await cursor.close()

    logging.warning('Bye!')


if __name__ == '__main__':
    # executor.start_webhook(
    #     dispatcher=dp,
    #     webhook_path=WEBHOOK_PATH,
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT
    # )
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)