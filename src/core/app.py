from abc import ABC, abstractmethod

from src.core.input.message_handlers.events.bot_events import BotEvents
from src.core.page.page_factory import PageFactory
from src.core.user.user_base import UserBase


class App(ABC):
    """
    The root object of bot.
    """

    def __init__(self, bot):
        self.bot = bot
        self._page_fac: PageFactory = None
        self.navigator = None
        self.user_input = None
        self.users = UserBase()
        self.events = BotEvents()

        self.initialize(bot)

    @abstractmethod
    def start(self):
        """
        Call this method to start listening for connections.
        """
        pass

    @abstractmethod
    def initialize(self, bot):
        pass

    def add_page(self, page_data):
        """
        Add the PageData model to be handled by bot.
        """
        self.navigator.add_page_data(page_data)
