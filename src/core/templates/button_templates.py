from src.core.input.keyboard.button.button_data import ButtonData, ButtonCallback


class ButtonTemplates:
    def __init__(self, navigation):
        self._nav = navigation

    def set(self, key, template: ButtonData):
        self.__dict__.update({key: template})

    def add_default_navigation(self, back_text, home_text):
        self.set('Back', ButtonData(back_text, ButtonCallback(self._nav.get_back)))
        self.set('Home', ButtonData(home_text, ButtonCallback(self._nav.change_page, path=f"~/")))
