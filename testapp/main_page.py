from src.button.button_data import ButtonData, ButtonCallback
from src.button.button_function import ButtonFunction
from src.page.page import Page


class MainPage(Page):
    async def handle_contact(self, user, phone):
        await self._send_message(user, f"Номер {phone} получен")

    def _initialize(self, markup_factory):
        super()._initialize(markup_factory)
        self.bot_events.subscribe_contact_share(self.handle_contact)

    async def make_render_content(self, user):
        useless_button = ButtonData("Useless", ButtonCallback(self._send_message,
                                                              message=f"User {user.id} has pressed an useless button!"))
        info_button = ButtonData("Info", ButtonCallback(self.navigator.change_page, path='/info'))
        bottom_button = ButtonData("Phone", None,
                                   ButtonFunction.request_phone)
        self.markup.add_row([
            useless_button,
            info_button
        ])
        self.markup.add_row([bottom_button])
        await self._send_keyboard_message(user, self.markup, 'Press this fucking button!')
