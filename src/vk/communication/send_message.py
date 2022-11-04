from random import randrange

from src.core.communication.send_message import SendMessage


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
