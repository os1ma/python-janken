class Janken:
    def __init__(self, janken_id, played_at):
        self._janken_id = janken_id
        self._played_at = played_at

    @property
    def janken_id(self):
        return self._janken_id

    @property
    def played_at(self):
        return self._played_at
