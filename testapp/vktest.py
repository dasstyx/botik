import vk_api

from src.app.app import App
from src.app.tg_app import TgApp
from src.app.vk_app import VkApp
from src.page.page_data import PageData
from testapp.info_page import InfoPage
from testapp.main_page import MainPage

token = '5459388993:AAF-F4kFuLLpAhhh1imTQ3uXEO72VddnBsU'
bot = vk_api.VkApi(token=token)

app = VkApp(bot)

app.add_page(PageData(MainPage, '/', inline=True, one_time=True))
app.add_page(PageData(InfoPage, '/info', Inline=True, one_time=True))

bot.infinity_polling()
