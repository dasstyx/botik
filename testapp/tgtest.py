from telebot.async_telebot import AsyncTeleBot

from src.app.tg_app import TgApp
from src.page.page_data import PageData
from testapp.info_page import InfoPage
from testapp.main_page import MainPage

token = ''
bot = AsyncTeleBot(token)

app = TgApp(bot)

app.add_page(PageData(MainPage, '/', inline=False, one_time=True))
app.add_page(PageData(InfoPage, '/info', Inline=True, one_time=True))

app.start()
