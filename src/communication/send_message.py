from abc import ABC


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

    def send(self, user, text):
        self.bot.messages.send(peer_id=user.id, message=text)

    def send_with_keyboard(self, user, text, keyboard):
        markup = keyboard.get_native_markup()
        self.bot.messages.send(peer_id=user.id, keyboard=markup.get_keyboard(), message=text)