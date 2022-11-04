from abc import ABC


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
