from abc import ABC
from random import randrange


class SendMessage(ABC):
    def __init__(self, bot):
        self.bot = bot

    def send(self, user, text):
        pass

    def send_with_keyboard(self, user, text, keyboard):
        pass

class TgSendMessage(SendMessage):

    def send(self, user, text):
        self.bot.send_message(user.id, text)

    def send_with_keyboard(self, user, text, keyboard):
        markup = keyboard.get_native_markup()
        self.bot.send_message(user.id, text, reply_markup=markup)

class VkSendMessage(SendMessage):

    def __init__(self, raw_api):
        self.raw_api = raw_api

    def send(self, user, text):
        uid = user.id
        self.raw_api.messages.send(user_ids=uid, random_id=randrange(10e10), peer_id=uid,
                                   message=text)

    def send_with_keyboard(self, user, text, keyboard):
        uid = user.id
        markup = keyboard.get_native_markup()
        self.raw_api.messages.send(user_ids=uid, random_id=randrange(10e10), peer_id=uid,
                                   message=text, keyboard=markup.get_keyboard())