import telebot

from src.app.app import App, TgApp
from src.page.page_data import PageData
from testapp.info_page import InfoPage
from testapp.main_page import MainPage

token = ''
bot = telebot.TeleBot(token)

app = TgApp(bot)

app.add_page(PageData(MainPage, '/', inline=True, one_time=True))
app.add_page(PageData(InfoPage, '/info', Inline=True, one_time=True))

bot.infinity_polling()
