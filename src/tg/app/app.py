import asyncio

from src.core.app.app import App
from src.tg.app.message_handlers.tg_raw_message_handlers import TgRawMessageHandlers
from src.core.app.user_input import UserInput
from src.tg.communication.api import TgApi
from src.core.navigation.navigation import Navigation
from src.core.page.page_factory import PageFactory
from src.tg.page.page_factory import TgPageFactory


class TgApp(App):
    def start(self):
        asyncio.run(self.bot.polling())

    def __init__(self, bot, start_callback=None):
        super().__init__(bot)
        self.message_handlers = TgRawMessageHandlers(bot, start_callback,
                                                     self.users, self.navigator,
                                                     self.user_input, self.events)

    def initialize(self, bot):
        api = TgApi(bot)
        self.navigator = Navigation()

        self._page_fac: PageFactory = TgPageFactory(api, self.navigator, self.events)
        self.navigator.init_page_factory(self._page_fac)

        self.user_input = UserInput(self.navigator, self.users)
