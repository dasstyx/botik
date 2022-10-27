from vkbottle import API
from vkbottle.bot import Bot

from src.app.vk_app import VkApp
from src.page.page_data import PageData
from testapp.info_page import InfoPage
from testapp.main_page import MainPage
from testapp.native_args_page import NativeArgsPage
from testapp.phone_page import PhonePage

token = ""
bot = Bot(token=token)
bot_api = API(token)

app = VkApp(bot, bot_api)

app.add_page(PageData(MainPage, '/', inline=True, one_time=True))
app.add_page(PageData(NativeArgsPage, '/nargs', inline=False, one_time=False))
app.add_page(PageData(InfoPage, '/info', Inline=False, one_time=False))
app.add_page(PageData(PhonePage, '/phone', Inline=False, one_time=False))

bot.run_forever()
