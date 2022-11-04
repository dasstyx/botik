from src.core.page.page_data import PageData
from src.core.page.page_factory import PageFactory
from src.tg.input.keyboard.button.button_factory import TgButtonFactory
from src.tg.input.keyboard.markup_factory import TgKeyboardMarkupFactory


class TgPageFactory(PageFactory):
    def _make_dependencies(self, page_data: PageData):
        button_factory = TgButtonFactory(page_data.inline)
        self.markup_factory = TgKeyboardMarkupFactory(button_factory)
