from src.core.api.api import Api, ApiType
from src.tg.api.send_message import TgSendMessage


class TgApi(Api):
    def __init__(self, bot):
        self.msg = TgSendMessage(bot)
        self.api_type = ApiType.Tg
