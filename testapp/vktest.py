import os

from vkbottle import API
from vkbottle.bot import Bot

from src.app.vk_app import VkApp
from pages_data import *
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('vk_token')
bot = Bot(token=token)
bot_api = API(token)

app = VkApp(bot, bot_api)

pages = [main_data, info_data, phone_data, nargs_data, stub1_data, stub2_data]
for page in pages:
    app.add_page(page)


bot.run_forever()
