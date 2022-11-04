from src.core.button.button_function import ButtonFunction


class ButtonCallback:
    def __init__(self, func, **kwargs):
        self.kwargs = kwargs
        self.func = func

    async def invoke(self, **kwargs) -> None:
        """
        Invoke the function with the given arguments.

        Args:
            **kwargs: The arguments to pass to the function.
        """
        await self.func(**self.kwargs, **kwargs)


class ButtonData:
    default_function = ButtonFunction.default

    def __init__(self, text: str, callback: ButtonCallback,
                 button_function: ButtonFunction = default_function, **native_args):
        """
        :param text: The text to display on the button.
        :param callback: The callback to call when the button is clicked.
        :param button_function: The Enum value of specific button type. For example, the 'share contact' button type.
        :param native_args: Any arguments to pass to the backbone API button's constructor.
        """
        self.native_args = native_args
        self.button_function = button_function
        self.callback = callback
        self.text = text