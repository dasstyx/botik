from abc import ABC

from src.core.api.send_message import SendMessage


class Api(ABC):
    def __init__(self, bot):
        self.msg: SendMessage = None
        self.api_type = None
