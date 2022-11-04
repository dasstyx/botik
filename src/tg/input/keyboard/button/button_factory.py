from src.core.input.keyboard.button.button_factory import ButtonFactory
from src.tg.input.keyboard.button.button import TgButton


class TgButtonFactory(ButtonFactory):
    button_type = TgButton
