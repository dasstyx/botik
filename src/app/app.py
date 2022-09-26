from abc import ABC, abstractmethod

from src.page.page_data import PageData
from src.page.page_factory import PageFactory
from src.user.user_base import UserBase


class App(ABC):
    default_data = PageData(False, False)

    def __init__(self, bot):
        self.bot = bot
        self._page_fac: PageFactory = None
        self.navigator = None
        self.user_input = None
        self.users = UserBase()

        self.initialize(bot)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def initialize(self, bot):
        pass

    def add_page(self, page_data=default_data):
        # page = self._page_fac.create(page_type, route, page_data)
        self.navigator.add_page_data(page_data)


