from telebot.async_telebot import AsyncTeleBot

from src.app.tg_app import TgApp
from src.page.page_data import PageData
from testapp.info_page import InfoPage
from testapp.main_page import MainPage
from testapp.native_args_page import NativeArgsPage

token = ''
bot = AsyncTeleBot(token)

app = TgApp(bot)

app.add_page(PageData(MainPage, '/', inline=False, one_time=True))
app.add_page(PageData(NativeArgsPage, '/nargs', inline=False, one_time=False))
app.add_page(PageData(InfoPage, '/info', inline=True, one_time=True))

app.start()
