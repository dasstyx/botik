from abc import ABC, abstractmethod

from src.app.message_handlers.events.events_backbone import event


class BotEvent(ABC):
    @abstractmethod
    def subscribe(self, func):
        self.__call__ += func

    @abstractmethod
    def unsubscribe(self, func):
        self.__call__ -= func

    @abstractmethod
    @event
    def __call__(self):
        pass
