from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from src.app.message_handlers.events.bot_event import BotEvent


class TestBotEvent(IsolatedAsyncioTestCase):
    event_triggers = 0

    async def test_subscribe(self):
        event = self.create_event()
        event.subscribe(self.event_target)
        event.subscribe(self.event_target2)

        await event(None, None)
        self.assertEqual(self.event_triggers, 2)

    async def test_unsubscribe(self):
        event = self.create_event()
        event.subscribe(self.event_target)
        event.subscribe(self.event_target2)

        event.unsubscribe(self.event_target)
        await event(None, None)
        self.assertEqual(self.event_triggers, 1)

    async def test_duplicate_subscriptions(self):
        event = self.create_event()
        for _ in range(5):
            event.subscribe(self.event_target)
        event.subscribe(self.event_target2)

        await event(None, None)
        self.assertEqual(self.event_triggers, 2)

    async def event_target(self, user, arg):
        self.event_triggers += 1

    async def event_target2(self, user, arg):
        await self.event_target(user, arg)

    @patch.object(BotEvent, '__abstractmethods__', set())
    def create_event(self):
        event = BotEvent()
        return event
