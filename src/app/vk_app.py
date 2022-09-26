from src.app.app import App
from src.app.user_input import UserInput
from src.communication.api import VKApi
from src.navigation.navigation import Navigation
from src.page.page_factory import PageFactory, VkPageFactory
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class VkApp(App):
    def start(self):
        longpoll = VkBotLongPoll(self.bot)

    def __init__(self, bot, start_callback=None):
        super().__init__(bot)

    def initialize(self, bot):
        api = VKApi(bot)
        self.navigator = Navigation()

        self._page_fac: PageFactory = VkPageFactory(api, self.navigator)
        self.navigator.init_page_factory(self._page_fac)

        self.user_input = UserInput(self.navigator, self.users)