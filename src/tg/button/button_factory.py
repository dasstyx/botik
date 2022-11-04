from src.core.button.button_factory import ButtonFactory
from src.tg.button.button import TgButton


class TgButtonFactory(ButtonFactory):
    button_type = TgButton
