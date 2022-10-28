from src.app.message_handlers.raw_message_handlers import RawMessageHandlers


class TgRawMessageHandlers(RawMessageHandlers):
    def _initialize_handlers(self, bot):
        bot.message_handler(content_types=['text'])(self.message_reply)
        bot.message_handler(content_types=['contact'])(self.phone_reply)
        bot.message_handler(content_types=['location'])(self.location_reply)
        bot.message_handler(commands=['start'])(self.start_reply)

        bot.callback_query_handler(func=lambda call: True)(self.callbacks_handle)

    async def _get_user_from_message(self, message):
        user_id = message.from_user.id
        return await self._get_user_from_id(user_id)

    async def callbacks_handle(self, call):
        data = call.data

        user_id = call.from_user.id
        user = await self._get_user_from_id(user_id)

        await self.user_input.forward_inline_button(user, data)

    async def location_reply(self, message):
        user = await self._get_user_from_message(message)
        location = message.location

        await user.storage.add_entry("location", location)
        self.events.geo_share(user, location)

    async def phone_reply(self, message):
        user = await self._get_user_from_message(message)
        number = message.contact.phone_number
        print(f"Got a number! {number}")

        await user.storage.add_entry("phone", number)
        await self.events.contact_share(user, number)
