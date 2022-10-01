from src.button.button_data import ButtonData
from src.page.page import Page


class InfoPage(Page):

    def _respond_to_input(self, user, text):
        self.send_message(user, f"Нет, ты {text}")

    async def make_render_content(self, user):
        info_button = ButtonData("Back", lambda user: self.navigator.get_back(user))
        self.markup.add_row([
            info_button
        ])
        self._send_keyboard_message(user, self.markup, 'Ну ты можешь вернуться...')