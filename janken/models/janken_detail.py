from models.hand import Hand
from models.result import Result


class JankenDetail:
    def __init__(
            self,
            janken_detail_id: int,
            janken_id: int,
            player_id: int,
            hand: Hand,
            result: Result):
        self._janken_detail_id = janken_detail_id
        self._janken_id = janken_id
        self._player_id = player_id
        self._hand = hand
        self._result = result

    @property
    def janken_detail_id(self) -> int:
        return self._janken_detail_id

    @property
    def janken_id(self) -> int:
        return self._janken_id

    @property
    def player_id(self) -> int:
        return self._player_id

    @property
    def hand(self) -> Hand:
        return self._hand

    @property
    def result(self) -> Result:
        return self._result
