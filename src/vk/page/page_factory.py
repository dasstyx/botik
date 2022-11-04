from src.core.page.page_data import PageData
from src.core.page.page_factory import PageFactory
from src.vk.button.button_factory import VkButtonFactory
from src.vk.keyboard.markup_factory import VkKeyboardMarkupFactory


class VkPageFactory(PageFactory):
    def _make_dependencies(self, page_data: PageData):
        button_factory = VkButtonFactory(page_data.inline)
        self.markup_factory = VkKeyboardMarkupFactory(button_factory)
