from src.core.button.button_factory import ButtonFactory
from src.vk.button.button import VkButton


class VkButtonFactory(ButtonFactory):
    button_type = VkButton
