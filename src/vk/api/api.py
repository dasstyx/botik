from src.core.api.api import Api, ApiType
from src.vk.api.send_message import VkSendMessage


class VKApi(Api):
    def __init__(self, raw_api):
        self.msg = VkSendMessage(raw_api)
        self.api_type = ApiType.Vk
