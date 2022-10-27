from abc import ABC, abstractmethod

from src.page.page import Page


class InputPage(Page, ABC):

    @abstractmethod
    async def success(self, user, text):
        pass

    async def fail(self, user, text):
        pass

    async def filter_input(self, user, text):
        return True

    async def _respond_to_input(self, user, text):
        if await self.filter_input(user, text):
            await self.success(user, text)
        else:
            await self.fail(user, text)
