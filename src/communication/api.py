from abc import ABC
from enum import Enum

from src.communication.send_message import TgSendMessage, VkSendMessage, SendMessage


class ApiType(Enum):
    Tg = 1
    Vk = 2

class Api(ABC):
    def __init__(self, bot):
        self.msg:SendMessage = None

class TgApi(Api):
    def __init__(self, bot):
        self.msg = TgSendMessage(bot)
        self.api_type = ApiType.Tg

class VKApi(Api):
    def __init__(self, raw_api):
        self.msg = VkSendMessage(raw_api)
        self.api_type = ApiType.Vk
