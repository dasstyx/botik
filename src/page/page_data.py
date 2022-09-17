from abc import ABC
from typing import Type

from src.page.page import Page


class PageData(ABC):
    def __init__(self, page_type: Type[Page], path: str, inline=False, one_time=False, **dependencies):
        self.path = path
        self.page_type = page_type
        self.one_time = one_time
        self.inline = inline
        self.__dict__.update(dependencies)


# class TgPageData(PageData):
#     pass
