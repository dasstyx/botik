from typing import Callable, Any

from src.app.message_handlers.events.bot_event import BotEvent
from src.app.message_handlers.events.events_backbone import event
from src.user.user import User


class ContactShareEvent(BotEvent):
    def subscribe(self, func: Callable[[User, str], Any]):
        super().subscribe(func)

    def unsubscribe(self, func: Callable[[User, str], Any]):
        super().subscribe(func)
