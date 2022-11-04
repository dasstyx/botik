from src.core.api.api import Api
from src.tg.api.api_type import TgApiType
from src.tg.api.send_message import TgSendMessage


class TgApi(Api):
    def __init__(self, bot):
        self.msg = TgSendMessage(bot)
        self.api_type = TgApiType()
