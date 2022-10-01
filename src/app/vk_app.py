from vkbottle.dispatch.rules.base import GeoRule, PayloadRule

from src.app.app import App
from src.app.user_input import UserInput
from src.communication.api import VKApi
from src.navigation.navigation import Navigation
from src.page.page_factory import PageFactory, VkPageFactory

class VkRawMessageHandlers:
    def __init__(self, bot, start_callback, users, navigator, user_input):
        self.user_input = user_input
        self.navigator = navigator
        self.users = users
        self.start_callback = start_callback

        bot.on.private_message()(self.message_reply)
        bot.on.private_message(GeoRule())(self.location_reply)
        bot.on.private_message(text=["Начать"])(self.start_reply)

        check_inline = lambda m: m.get_payload_json().get("inline", None)
        bot.on.private_message(func=check_inline)(self.callbacks_handle)

    async def start_reply(self, message):
        user = await self._get_user_from_message(message)

        if self.start_callback:
            await self.start_callback(user)

    async def message_reply(self, message):
        user = await self._get_user_from_message(message)
        await self.user_input.handle_input(user, message.text)

    async def _get_user_from_message(self, message):
        user_id = message.from_id
        return await self._get_user_from_id(user_id)

    async def _get_user_from_id(self, user_id):
        if self.users.exists(user_id):
            user = self.users.get(user_id)
            print(f"Existing user! id: {user.id}")
        else:
            user = self.users.add(user_id)
            await self.navigator.change_page(user, '/')
            print(f"New user! id: {user.id}")
        return user

    async def callbacks_handle(self, call):
        data = call.get_payload_json().get("inline")

        user_id = call.from_id
        user = await self._get_user_from_id(user_id)

        await self.user_input.forward_inline_button(user, data)

    async def location_reply(self, message):
        user = await self._get_user_from_message(message)
        location = message.geo

        await user.storage.add_entry("location", location)


class VkApp(App):
    def start(self):
        self.bot.run_forever()

    def __init__(self, bot, raw_api, start_callback=None):
        super().__init__(bot)
        # self.raw_api = raw_api
        self.initialize_with_raw_api(raw_api)
        self.message_handlers = VkRawMessageHandlers(bot, start_callback,
                                                     self.users, self.navigator,
                                                     self.user_input)

    def initialize(self, bot):
        pass

    def initialize_with_raw_api(self, raw_api):
        api = VKApi(raw_api)
        self.navigator = Navigation()

        self._page_fac: PageFactory = VkPageFactory(api, self.navigator)
        self.navigator.init_page_factory(self._page_fac)

        self.user_input = UserInput(self.navigator, self.users)