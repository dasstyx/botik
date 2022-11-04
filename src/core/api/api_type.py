from typing import Type


class ApiType:

    def __eq__(self, o: Type) -> bool:
        return type(self) == o
