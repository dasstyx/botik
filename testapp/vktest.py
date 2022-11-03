import logging
import os
import sys

root_path = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_path)

from dotenv import load_dotenv
from vkbottle import API
from vkbottle.bot import Bot

from pages_data import *
from src.app.vk_app import VkApp

load_dotenv()

logging.getLogger().setLevel(logging.DEBUG)

token = os.getenv('vk_token')
bot = Bot(token=token)
bot_api = API(token)

app = VkApp(bot, bot_api)

pages = [main_data, info_data, phone_data, nargs_data, stub1_data, stub2_data]
for page in pages:
    app.add_page(page)

bot.run_forever()
