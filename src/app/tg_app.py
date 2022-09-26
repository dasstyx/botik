import telebot

from src.app.app import App
from src.app.user_input import UserInput
from src.communication.api import TgApi
from src.navigation.navigation import Navigation
from src.page.page_factory import PageFactory, TgPageFactory


class TgRawMessageHandlers:
    def __init__(self, bot, start_callback, users, navigator, user_input):
        self.user_input = user_input
        self.navigator = navigator
        self.users = users
        self.start_callback = start_callback

        bot.message_handler(content_types=['text'])(self.message_reply)
        bot.message_handler(content_types=['contact'])(self.phone_reply)
        bot.message_handler(content_types=['location'])(self.location_reply)
        bot.message_handler(commands=['start'])(self.start_reply)

        bot.callback_query_handler(func=lambda call: True)(self.callbacks_handle)

    def _get_user_from_message(self, message):
        user_id = message.from_user.id
        return self._get_user_from_id(user_id)

    def _get_user_from_id(self, user_id):
        if self.users.exists(user_id):
            user = self.users.get(user_id)
            print(f"Existing user! id: {user.id}")
        else:
            user = self.users.add(user_id)
            self.navigator.change_page(user, '/')
            print(f"New user! id: {user.id}")
        return user

    def callbacks_handle(self, call):
        data = call.data

        user_id = call.from_user.id
        user = self._get_user_from_id(user_id)

        self.user_input.forward_inline_button(user, data)

    def start_reply(self, message):
        user = self._get_user_from_message(message)

        if self.start_callback:
            self.start_callback(user)

    def message_reply(self, message):
        user = self._get_user_from_message(message)
        self.user_input.handle_input(user, message.text)

    def location_reply(self, message):
        user = self._get_user_from_message(message)
        location = message.location

        user.storage.add_entry("location", location)

    def phone_reply(self, message):
        user = self._get_user_from_message(message)
        number = message.contact.phone_number
        print(f"Got a number! {number}")

        user.storage.add_entry("phone", number)


class TgApp(App):
    def start(self):
        self.bot.infinity_polling()

    def __init__(self, bot:telebot.TeleBot, start_callback=None):
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


