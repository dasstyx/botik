from abc import ABC

from src.button.button_function import ButtonFunction


class ButtonCallback:
    def __init__(self, func, **kwargs):
        self.kwargs = kwargs
        self.func = func

    async def invoke(self, **kwargs):
        await self.func(**self.kwargs, **kwargs)


class ButtonData:
    default_function = ButtonFunction.default

    def __init__(self, text, callback: ButtonCallback, button_function: ButtonFunction = default_function):
        self.button_function = button_function
        self.callback = callback
        self.text = text

