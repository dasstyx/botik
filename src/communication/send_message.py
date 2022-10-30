from abc import ABC
from random import randrange


class SendMessage(ABC):
    """
    API wrapper for sending messages.
    """
    def __init__(self, bot):
        self.bot = bot

    async def send(self, user, text):
        pass

    async def send_with_keyboard(self, user, text, keyboard):
        pass


class TgSendMessage(SendMessage):

    async def send(self, user, text):
        await self.bot.send_message(user.id, text)

    async def send_with_keyboard(self, user, text, keyboard):
        markup = keyboard.get_native_markup()
        await self.bot.send_message(user.id, text, reply_markup=markup)


class VkSendMessage(SendMessage):

    def __init__(self, raw_api):
        self.raw_api = raw_api

    async def send(self, user, text):
        uid = user.id
        await self.raw_api.messages.send(user_id=uid, random_id=randrange(10e10),
                                         message=text)

    async def send_with_keyboard(self, user, text, keyboard):
        uid = user.id
        markup = keyboard.get_native_markup()
        await self.raw_api.messages.send(user_id=uid, random_id=randrange(10e10),
                                         message=text, keyboard=markup)
