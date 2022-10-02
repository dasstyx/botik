from src.app.app import App
from src.app.message_handlers.vk_raw_message_handlers import VkRawMessageHandlers
from src.app.user_input import UserInput
from src.communication.api import VKApi
from src.navigation.navigation import Navigation
from src.page.page_factory import PageFactory, VkPageFactory


class VkApp(App):
    def start(self):
        self.bot.run_forever()

    def __init__(self, bot, raw_api, start_callback=None):
        super().__init__(bot)
        # self.raw_api = raw_api
        self.initialize_with_raw_api(raw_api)
        self.message_handlers = VkRawMessageHandlers(bot, start_callback,
                                                     self.users, self.navigator,
                                                     self.user_input, self.events)

    def initialize(self, bot):
        pass

    def initialize_with_raw_api(self, raw_api):
        api = VKApi(raw_api)
        self.navigator = Navigation()

        self._page_fac: PageFactory = VkPageFactory(api, self.navigator, self.events)
        self.navigator.init_page_factory(self._page_fac)

        self.user_input = UserInput(self.navigator, self.users)
