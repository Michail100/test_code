from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from config import get_fromenv
from sql import create_pool, create_db

bot = Bot(token=get_fromenv('TOKEN'), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
loop = asyncio.get_event_loop()
cursor = loop.run_until_complete(create_pool())

