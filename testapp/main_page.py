from src.button.button_data import ButtonData
from src.page.page import Page


class MainPage(Page):
    async def make_render_content(self, user):
        useless_button = ButtonData("Useless", lambda user: self.send_message(user, f"User {user.id} has pressed an useless button!"))
        info_button = ButtonData("Info", lambda user: self.navigator.change_page(user, '/info'))
        bottom_button = ButtonData("Row 2", None)
        self.markup.add_row([
            useless_button,
            info_button
        ])
        self.markup.add_row([bottom_button])
        await self._send_keyboard_message(user, self.markup, 'Press this fucking button!')
