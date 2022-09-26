import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union, Type

from src.button.button_factory import TgButtonFactory, VkButtonFactory
from src.keyboard.markup_factory import TgKeyboardMarkupFactory, VkKeyboardMarkupFactory
from src.page.page import Page
from src.page.page_data import PageData


class PageFactory(ABC):

    def __init__(self, api, navigator):
        self.navigator = navigator
        self.api = api

    @abstractmethod
    def _make_dependencies(self, page_data: PageData):
        pass

    def create(self, data: PageData):
        # if type(path) is str:
        #     path = Path(path)
        # elif type(Path):
        #     path = path
        # else:
        #     logging.warning("Unsupported path type")

        self._make_dependencies(data)
        return data.page_type(data.path, self.api, self.navigator, self.markup_factory, data)


class TgPageFactory(PageFactory):
    def _make_dependencies(self, page_data: PageData):
        button_factory = TgButtonFactory(page_data.inline)
        self.markup_factory = TgKeyboardMarkupFactory(button_factory)


class VkPageFactory(PageFactory):
    def _make_dependencies(self, page_data: PageData):
        button_factory = VkButtonFactory(page_data.inline)
        self.markup_factory = VkKeyboardMarkupFactory(button_factory)
