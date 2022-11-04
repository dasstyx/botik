from src.core.api.api import Api
from src.core.api.api_type import ApiType
from src.vk.api.api_type import VkApiType
from src.vk.api.send_message import VkSendMessage


class VKApi(Api):
    def __init__(self, raw_api):
        self.msg = VkSendMessage(raw_api)
        self.api_type = VkApiType()
