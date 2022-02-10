# -*- coding: UTF-8 -*-
from aiogram import Dispatcher,types, Bot
from aiogram.dispatcher.filters import Text
from config import get_fromenv
from asyncio import sleep


def gen_any_kbrd(call_back_data,row_width,**kwargs):
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    keys = [types.InlineKeyboardButton(kwargs[key], callback_data=key[0] + key[-1] + call_back_data) for key in kwargs]
    keyboard.add(*keys)
    return keyboard