from typing import Callable, Any

from src.app.message_handlers.events.contact_share_event import ContactShareEvent
from src.app.message_handlers.events.events_backbone import event
from src.app.message_handlers.events.geo_share_event import GeoShareEvent
from src.user.user import User


class BotEvents:
    def __init__(self):
        self.contact_share = ContactShareEvent()
        self.geo_share = GeoShareEvent()

    def subscribe_contact_share(self, func: Callable[[User, str], Any]):
        self.contact_share += func

    def unsubscribe_contact_share(self, func: Callable[[User, str], Any]):
        self.contact_share -= func

    def subscribe_geo_share(self, func: Callable[[User, Any], Any]):
        self.geo_share += func

    def unsubscribe_geo_share(self, func: Callable[[User, Any], Any]):
        self.geo_share -= func

    @event
    async def contact_share(self):
        pass

    @event
    async def geo_share(self):
        pass
