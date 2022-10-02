from abc import ABC, abstractmethod

from src.app.message_handlers.bot_events import BotEvents


class RawMessageHandlers(ABC):
    def __init__(self, bot, start_callback, users, navigator, user_input, events):
        self.events = events
        self.user_input = user_input
        self.navigator = navigator
        self.users = users
        self.start_callback = start_callback

        self._initialize_handlers(bot)

    @abstractmethod
    def _initialize_handlers(self, bot):
        pass

    @abstractmethod
    async def _get_user_from_message(self, message):
        pass

    async def _get_user_from_id(self, user_id):
        if self.users.exists(user_id):
            user = self.users.get(user_id)
            print(f"Existing user! id: {user.id}")
        else:
            user = self.users.add(user_id)
            await self.navigator.change_page(user, '/')
            print(f"New user! id: {user.id}")
        return user

    async def start_reply(self, message):
        user = self._get_user_from_message(message)

        if self.start_callback:
            await self.start_callback(user)

    async def message_reply(self, message):
        user = await self._get_user_from_message(message)
        await self.user_input.handle_input(user, message.text)