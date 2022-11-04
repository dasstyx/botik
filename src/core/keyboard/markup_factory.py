from abc import ABC, abstractmethod


class KeyboardMarkupFactory(ABC):
    def __init__(self, button_factory):
        self.button_factory = button_factory

    @abstractmethod
    def create(self, **native_args):
        """
        :param native_args: Any arguments to pass to the backbone API keyboard markup's constructor.
        """
        pass

