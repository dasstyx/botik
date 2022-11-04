from vkbottle import Text

from src.core.input.keyboard.button.button import Button


class VkButton(Button):
    def _create_native(self):
        # TODO: Add a geo button type if possible
        text = self.get_text()
        data = {"action": Text(text)}
        data.update(self.native_args)
        self.native_data = data
