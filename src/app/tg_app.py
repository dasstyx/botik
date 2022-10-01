import telebot

from src.app.app import App
from src.app.raw_message_handlers import RawMessageHandlers
from src.app.user_input import UserInput
from src.communication.api import TgApi
from src.navigation.navigation import Navigation
from src.page.page_factory import PageFactory, TgPageFactory

import asyncio


class TgRawMessageHandlers(RawMessageHandlers):
    def _initialize_handlers(self, bot):
        bot.message_handler(content_types=['text'])(self.message_reply)
        bot.message_handler(content_types=['contact'])(self.phone_reply)
        bot.message_handler(content_types=['location'])(self.location_reply)
        bot.message_handler(commands=['start'])(self.start_reply)

        bot.callback_query_handler(func=lambda call: True)(self.callbacks_handle)

    async def _get_user_from_message(self, message):
        user_id = message.from_user.id
        return await self._get_user_from_id(user_id)

    async def callbacks_handle(self, call):
        data = call.data

        user_id = call.from_user.id
        user = await self._get_user_from_id(user_id)

        await self.user_input.forward_inline_button(user, data)

    async def location_reply(self, message):
        user = await self._get_user_from_message(message)
        location = message.location

        await user.storage.add_entry("location", location)

    async def phone_reply(self, message):
        user = await self._get_user_from_message(message)
        number = message.contact.phone_number
        print(f"Got a number! {number}")

        await user.storage.add_entry("phone", number)


class TgApp(App):
    def start(self):
        asyncio.run(self.bot.polling())

    def __init__(self, bot, start_callback=None):
        super().__init__(bot)
        self.message_handlers = TgRawMessageHandlers(bot, start_callback,
                                                     self.users, self.navigator,
                                                     self.user_input)

    def initialize(self, bot):
        api = TgApi(bot)
        self.navigator = Navigation()

        self._page_fac: PageFactory = TgPageFactory(api, self.navigator)
        self.navigator.init_page_factory(self._page_fac)

        self.user_input = UserInput(self.navigator, self.users)
