from abc import ABC, abstractmethod
from pathlib import Path

from src.app.message_handlers.bot_events import BotEvents
from src.communication.api import Api
from src.keyboard.keyboard_markup import KeyboardMarkup
from src.keyboard.markup_factory import KeyboardMarkupFactory


class Page(ABC):

    def __init__(self, path: str, api: Api, navigator, bot_events: BotEvents, markup_factory: KeyboardMarkupFactory, data):
        self.bot_events = bot_events
        self.nav = navigator
        self.api = api
        self.path = path

        self.markup_factory = markup_factory
        self._data = data
        self.markup: KeyboardMarkup = None

        self._initialize(markup_factory)

    def _initialize(self, markup_factory: KeyboardMarkupFactory):
        self._create_keyboard_markup(markup_factory)

    def _create_keyboard_markup(self, markup_factory):
        self.markup = markup_factory.create(self._data.inline, self._data.one_time)

    async def send(self, user, message, markup=False):
        if not markup:
            await self.api.msg.send(user, message)
        else:
            await self.api.msg.send_with_keyboard(user, message, self.markup)

    def get_data(self):
        return self._data

    def get_back_path(self):
        return str(Path(self.path).parent.as_posix())

    async def _respond_to_input(self, user, text):
        pass

    @abstractmethod
    async def make_page_content(self, user):
        pass

    async def handle_raw_input(self, user, text, only_check_press=False):
        # TODO: Don't trigger the inline buttons this way!
        pressed_button = self.markup.get_pressed_button(text)
        if pressed_button:
            await pressed_button.press(user)
        elif not only_check_press:
            await self._respond_to_input(user, text)
