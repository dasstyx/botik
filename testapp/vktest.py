from vkbottle import API

from vkbottle.bot import Bot
from src.app.app import App
from src.app.tg_app import TgApp
from src.app.vk_app import VkApp
from src.page.page_data import PageData
from testapp.info_page import InfoPage
from testapp.main_page import MainPage

token = ""
bot = Bot(token=token)
bot_api = API(token)

app = VkApp(bot, bot_api)

app.add_page(PageData(MainPage, '/', inline=True, one_time=True))
app.add_page(PageData(InfoPage, '/info', Inline=False, one_time=False))

bot.run_forever()
