from abc import ABC

from src.core.input.keyboard.button.button_data import ButtonData, ButtonCallback


class PageTemplates:
    def __init__(self, navigation) -> None:
        self.button = ButtonTemplates(navigation)


class ButtonTemplates:
    def __init__(self, navigation) -> None:
        self._nav = navigation
        self._templates = {}

    def set(self, key, template: ButtonData):
        self._templates[key] = template

    def save(self):
        self.__dict__.update(self._templates)
        self._templates.clear()

    def add_default_navigation(self, back_text, home_text):
        self.set('Back', ButtonData(back_text, ButtonCallback(self._nav.get_back)))
        self.set('Home', ButtonData(home_text, ButtonCallback(self._nav.change_page, path=f"~/")))
        self.save()
