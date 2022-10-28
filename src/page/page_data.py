from __future__ import annotations

from abc import ABC
from typing import Type, Union

from src.navigation.navigation import Navigation
from src.page.page import Page


class PageData(ABC):
    def __init__(self, page_type: Type[Page], path: str, parent: Union[str, PageData] = '',
                 inline=False, one_time=False, **dependencies):
        self.path = self._initialize_path(path, parent)
        self.page_type = page_type
        self.one_time = one_time
        self.inline = inline
        self.__dict__.update(dependencies)

    def _initialize_path(self, path, parent):
        if not parent:
            return path

        if not isinstance(parent, str):
            parent = parent.path

        combined_path = Navigation.concat_paths(parent, path)
        return str(combined_path)
