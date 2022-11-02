import logging
from abc import ABC
from typing import Callable, Any

from src.user.user import User


class BotEvent(ABC):
    def __init__(self) -> None:
        self.subscribers = set()

    def subscribe(self, func: Callable[[User, Any], Any]):
        if func in self.subscribers:
            logging.warning("Same function is subscribed multiple times")
        self.subscribers.add(func)

    def unsubscribe(self, func: Callable[[User, Any], Any]):
        self.subscribers.remove(func)

    async def __call__(self, user, argument):
        if len(self.subscribers) == 0:
            logging.warning("Zero subs")
        for subscriber in self.subscribers:
            await subscriber(user, argument)
