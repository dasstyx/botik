from src.core.input.keyboard.button.button_factory import ButtonFactory
from src.vk.input.keyboard.button.button import VkButton


class VkButtonFactory(ButtonFactory):
    button_type = VkButton
