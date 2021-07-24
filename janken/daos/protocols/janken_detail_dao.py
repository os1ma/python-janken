from typing import Protocol, List

from models.janken_detail import JankenDetail


class JankenDetailDao(Protocol):
    def count(self) -> int:
        ...

    def insert_all(self, janken_details: List[JankenDetail]) -> None:
        ...
