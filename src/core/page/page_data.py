from __future__ import annotations

from abc import ABC
from typing import Type, Union

from src.core.navigation.navigation import Navigation
from src.core.page.page import Page


class PageData(ABC):
    """
    The data of the page from which the instance will be created.
    """

    def __init__(self, page_type: Type[Page], path: str, parent: Union[str, PageData] = '',
                 inline=False, one_time=False, **dependencies):
        """
        :param page_type: The class type of the page to instantiate from.
        :param path: The relative path of the page. Will be concatenated with parent path string or Page object.
        :param parent: The parent path string or Page object of the page.
        :param inline: Whether the page is inline.
        :param one_time: Whether the page is one time.
        :param dependencies: Dependencies that the page can use at runtime.
        """
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