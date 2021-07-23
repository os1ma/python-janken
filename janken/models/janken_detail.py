class JankenDetail:
    def __init__(self, janken_detail_id, janken_id, player_id, hand, result):
        self._janken_detail_id = janken_detail_id
        self._janken_id = janken_id
        self._player_id = player_id
        self._hand = hand
        self._result = result

    @property
    def janken_detail_id(self):
        return self._janken_detail_id

    @property
    def janken_id(self):
        return self._janken_id

    @property
    def player_id(self):
        return self._player_id

    @property
    def hand(self):
        return self._hand

    @property
    def result(self):
        return self._result
