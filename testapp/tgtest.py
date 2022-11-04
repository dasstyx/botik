import logging
import os
import sys

root_path = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_path)

from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot

from pages_data import *
from src.app import TgApp

load_dotenv()

logging.getLogger().setLevel(logging.DEBUG)

token = os.getenv('tg_token')
bot = AsyncTeleBot(token)

app = TgApp(bot)

main_data.inline = False
info_data.inline = True
pages = [main_data, info_data, nargs_data, stub1_data, stub2_data]

for page in pages:
    app.add_page(page)

app.start()
