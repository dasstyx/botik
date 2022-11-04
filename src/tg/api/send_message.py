from src.core.api.send_message import SendMessage


class TgSendMessage(SendMessage):

    async def send(self, user, text):
        await self.bot.send_message(user.id, text)

    async def send_with_keyboard(self, user, text, keyboard):
        markup = keyboard.get_native_markup()
        await self.bot.send_message(user.id, text, reply_markup=markup)
