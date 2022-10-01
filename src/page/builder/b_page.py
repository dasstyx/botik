from pathlib import Path
from typing import Union

from src.page.builder.page_builder_model import PageBuilderModel
from src.page.page import Page
from src.page.page_data import PageData


class BPage(Page):

    def __init__(self, path: Union[str, Path], markup_factory, data: PageData):
        super().__init__(path, markup_factory, data)
        self.model = PageBuilderModel()

    def add_button(self, button):
        self.buttons.append(button)

    async def make_render_content(self, user):
        pass
