import re

from src.core.input.keyboard.button.button_data import ButtonCallback
from src.core.page.input_page import InputPage


class PhonePage(InputPage):
    async def success(self, user, text):
        await self.send(user, f"Номер {text} получен")
        await self.nav.change_page(user, '/')

    async def fail(self, user, text):
        await self.send(user, f"Некорректный номер")

    async def filter_input(self, user, text):
        return re.match(r"^(\+\d{1,3}[- ]?)?\d{10}$", text)

    async def make_page_content(self, user):
        from src.core.input.keyboard.button.button_data import ButtonData
        back_button = ButtonData("Back", ButtonCallback(self.nav.get_back))
        self.markup.add_row([back_button])

        await self.send(user, "Введите телефон", markup=True)
