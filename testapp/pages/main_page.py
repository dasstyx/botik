from vkbottle import KeyboardButtonColor
from src.core.api.api_type import ApiType
from src.core.input.keyboard.button.button_data import ButtonCallback, ButtonData
from src.core.input.keyboard.button.button_function import ButtonFunction
from src.core.page.page import Page
from src.vk.api.api_type import VkApiType


class MainPage(Page):
    async def handle_contact(self, user, phone):
        await self.send(user, f"Номер {phone} получен")

    def _initialize(self):
        self.bot_events.contact_share.subscribe(self.handle_contact)

    def destruct(self):
        self.bot_events.contact_share.unsubscribe(self.handle_contact)

    async def custom_callback(self, user, arg):
        await self.send(user, f"User {user.id} has pressed a custom callback button!\nThe argument is: {arg}")

    async def make_page_content(self, user):
        custom_callback_button = ButtonData("Custom callback", ButtonCallback(self.custom_callback, arg="foo-bar"))
        native_args_button = ButtonData("Native Args", ButtonCallback(self.nav.change_page, path='/nargs'))

        if self.api.api_type == VkApiType:
            bottom_button = ButtonData("Phone", ButtonCallback(self.nav.change_page, path='/phone'))
        else:
            bottom_button = ButtonData("Phone", None,
                                       ButtonFunction.request_phone)

        stub_page = ButtonData("Stub 1", ButtonCallback(self.nav.change_page, path='/stub1'))
        self.markup.add_row([
            custom_callback_button,
            native_args_button,
            stub_page
        ])
        if bottom_button:
            self.markup.add_row([bottom_button])
        await self.send(user, 'Main', markup=True)
