from typing import Callable, Any

from src.app.message_handlers.events.contact_share_event import ContactShareEvent
from src.app.message_handlers.events.geo_share_event import GeoShareEvent
from src.user.user import User


class BotEvents:
    def __init__(self):
        self.contact_share = ContactShareEvent()
        self.geo_share = GeoShareEvent()
