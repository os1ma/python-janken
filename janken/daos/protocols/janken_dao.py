from typing import Protocol

from models.janken import Janken


class JankenDao(Protocol):
    def count(self) -> int:
        ...

    def insert(self, janken: Janken) -> None:
        ...
