from vkbottle import KeyboardButtonColor

from src.core.api.api_type import ApiType
from src.core.input.keyboard.button.button_data import ButtonData, ButtonCallback
from src.core.page.page import Page
from src.tg.api.api_type import TgApiType
from src.vk.api.api_type import VkApiType


class NativeArgsPage(Page):
    def _create_keyboard_markup(self):
        if self.api.api_type == TgApiType:
            self.markup = self._markup_factory.create(inline=self._data.inline, one_time=self._data.one_time,
                                                      input_field_placeholder="Placeholder text")
        else:
            self.markup = self._markup_factory.create(inline=self._data.inline, one_time=self._data.one_time)

    async def make_page_content(self, user):
        if self.api.api_type == VkApiType:
            info_button = ButtonData("Primary", ButtonCallback(self.nav.change_page, path='~/info'),
                                     color=KeyboardButtonColor.PRIMARY)
        else:
            info_button = ButtonData("Primary", ButtonCallback(self.nav.change_page, path='~/info'))

        stub_page = ButtonData("Stub 1", ButtonCallback(self.nav.change_page, path='/stub1'))

        back_button = self.templates.button.Back
        self.markup.add_row([info_button, stub_page])
        self.markup.add_row([back_button])
        await self.send(user, 'This is native args page...', markup=True)
