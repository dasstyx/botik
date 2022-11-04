from abc import ABC, abstractmethod

from src.core.page.page_data import PageData


class PageFactory(ABC):

    def __init__(self, api, navigator, bot_events):
        self.bot_events = bot_events
        self.navigator = navigator
        self.api = api

    @abstractmethod
    def _make_dependencies(self, page_data: PageData):
        pass

    def create(self, data: PageData):
        self._make_dependencies(data)
        return data.page_type(data.path, self.api, self.navigator, self.bot_events, self.markup_factory, data)


