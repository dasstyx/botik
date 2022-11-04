import logging


class UserInput:
    def __init__(self, navigator, users):
        self.users = users
        self.navigator = navigator

    async def forward_inline_button(self, user, text):
        page = self.navigator.get_user_page(user)
        await page.handle_raw_input(user, text, True)
        logging.debug("Forward button")

    async def handle_input(self, user, text):
        # TODO: Do not render page on every user message!
        page = self.navigator.get_user_page(user)

        await page.handle_raw_input(user, text)
