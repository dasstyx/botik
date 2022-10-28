from telebot.async_telebot import AsyncTeleBot

from pages_data import *
from src.app.tg_app import TgApp

token = ''
bot = AsyncTeleBot(token)

app = TgApp(bot)

main_data.inline = False
info_data.inline = True
pages = [main_data, info_data, nargs_data, stub1_data, stub2_data]

for page in pages:
    app.add_page(page)

app.start()
