from vkbottle import KeyboardButtonColor

from src.button.button_data import ButtonData, ButtonCallback
from src.communication.api import ApiType
from src.page.page import Page


class NativeArgsPage(Page):
    def _create_keyboard_markup(self, markup_factory):
        if self.api.api_type == ApiType.Tg:
            self.markup = markup_factory.create(self._data.inline, self._data.one_time, row_width=6,
                                                resize_keyboard=True)
        else:
            self.markup = markup_factory.create(self._data.inline, self._data.one_time)

    async def make_page_content(self, user):
        if self.api.api_type == ApiType.Vk:
            info_button = ButtonData("Primary", ButtonCallback(self.nav.change_page, path='/info'),
                                     color=KeyboardButtonColor.PRIMARY)
        else:
            info_button = ButtonData("Primary", ButtonCallback(self.nav.change_page, path='/info'))

        back_button = ButtonData("Back", ButtonCallback(self.nav.get_back))
        self.markup.add_row([info_button])
        self.markup.add_row([back_button])
        await self.send(user, 'This is native args page...', markup=True)