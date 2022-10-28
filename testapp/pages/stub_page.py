from src.button.button_data import ButtonData, ButtonCallback
from src.page.page import Page


class StubPage(Page):
    async def make_page_content(self, user):
        num = self.get_data().num
        next_button = ButtonData("Next", ButtonCallback(self.nav.change_page, path=f"/stub{num + 1}"))
        back_button = ButtonData("Back", ButtonCallback(self.nav.get_back))
        home_button = ButtonData("Home", ButtonCallback(self.nav.change_page, path=f"~/"))

        self.markup.add_row([next_button])
        self.markup.add_row([back_button, home_button])
        await self.send(user, f"Stub {num}", markup=True)
