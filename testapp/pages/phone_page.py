import re

from src.button.button_data import ButtonData, ButtonCallback
from src.page.input_page import InputPage


class PhonePage(InputPage):
    async def success(self, user, text):
        # user.storage.add_entry("phone", text)
        await self.send(user, f"Номер {text} получен")
        await self.nav.change_page(user, '/')

    async def fail(self, user, text):
        await self.send(user, f"Некорректный номер")

    async def filter_input(self, user, text):
        return re.match(r"^(\+\d{1,3}[- ]?)?\d{10}$", text)

    async def make_page_content(self, user):
        back_button = ButtonData("Back", ButtonCallback(self.nav.get_back))
        self.markup.add_row([back_button])

        await self.send(user, "Введите телефон", markup=True)
