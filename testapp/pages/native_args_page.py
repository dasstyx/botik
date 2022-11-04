from vkbottle import KeyboardButtonColor

from src.button.button_data import ButtonData, ButtonCallback
from src.communication.api import ApiType
from src.page.page import Page


class NativeArgsPage(Page):
    def _create_keyboard_markup(self, markup_factory):
        if self.api.api_type == ApiType.Tg:
            self.markup = markup_factory.create(inline=self._data.inline, one_time=self._data.one_time,
                                                input_field_placeholder="Placeholder text")
        else:
            self.markup = markup_factory.create(inline=self._data.inline, one_time=self._data.one_time)

    async def make_page_content(self, user):
        if self.api.api_type == ApiType.Vk:
            info_button = ButtonData("Primary", ButtonCallback(self.nav.change_page, path='~/info'),
                                     color=KeyboardButtonColor.PRIMARY)
        else:
            info_button = ButtonData("Primary", ButtonCallback(self.nav.change_page, path='~/info'))

        stub_page = ButtonData("Stub 1", ButtonCallback(self.nav.change_page, path='/stub1'))

        back_button = ButtonData("Back", ButtonCallback(self.nav.get_back))
        self.markup.add_row([info_button, stub_page])
        self.markup.add_row([back_button])
        await self.send(user, 'This is native args page...', markup=True)
