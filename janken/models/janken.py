from datetime import datetime


class Janken:
    def __init__(self, janken_id: int, played_at: datetime):
        self._janken_id = janken_id
        self._played_at = played_at

    @property
    def janken_id(self) -> int:
        return self._janken_id

    @property
    def played_at(self) -> datetime:
        return self._played_at
