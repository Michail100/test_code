# -*- coding: UTF-8 -*-
from aiogram import Dispatcher,types, Bot
from aiogram.dispatcher.filters import Text
from config import get_fromenv
from asyncio import sleep
from database.database_handlers import insert_into_table,select_from_table, \
    update_table, delete_from_table, drop_id_key
import logging
from settings import dp


async def on_start(message: types.Message):
    await message.answer('<b>[INFO]</b> Hello testing <b>Postgres</b>')


async def insert_into_my_table(message: types.Message):
    try:
        res_id = await insert_into_table('Kolumb', 'Orel')
    except Exception as ex:
        logging.warning('[Error] log: insert', ex)
    finally:
        if isinstance(res_id, tuple):
            await message.answer('Insert - Ok')
        else:
            await message.answer(message.text)


async def select_row(message: types.Message):
    try:
        res_user = await select_from_table()
    except Exception as ex:
        logging.warning('[Error] log: select', ex)
    finally:
        if isinstance(res_user, tuple):
            await message.answer(f'Select - ok. Tuple - {res_user}')
        else:
            await message.answer(message.text)


async def update_users_table(message: types.Message):
    try:
        res = await update_table()
    except Exception as ex:
        logging.warning('[Error] log: update', ex)
    finally:
        if isinstance(res, bool) and res:
            await message.answer('Update - ok')
        else:
            await message.answer(message.text)


async def delete_data_from_table(message: types.Message):
    try:
        await delete_from_table()
        await message.answer('Delete - Ok')
        return
    except Exception as ex:
        print('[Error] log: delete', ex)


async def drop_id_data(message: types.Message):
    try:
        await drop_id_key()
        await message.answer('Drop - Ok')
        return
    except Exception as ex:
        print('[Error] log: drop', ex)


def register_base_handlers(dp: Dispatcher):
    dp.register_message_handler(on_start, commands='start', state='*')
    dp.register_message_handler(select_row, commands='get_data', state='*')
    dp.register_message_handler(insert_into_my_table, commands='insert_data', state='*')
    dp.register_message_handler(update_users_table, commands='update_data', state='*')
    dp.register_message_handler(delete_data_from_table, commands='delete_data', state='*')
    dp.register_message_handler(drop_id_data, commands='drop_id_key', state='*')
