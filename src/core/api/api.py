from abc import ABC
from enum import Enum

from src.core.api.send_message import SendMessage


class ApiType(Enum):
    Tg = 1
    Vk = 2


class Api(ABC):
    def __init__(self, bot):
        self.msg: SendMessage = None

