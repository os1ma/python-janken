class Player:
    def __init__(self, player_id, name):
        self._player_id = player_id
        self._name = name

    @property
    def player_id(self):
        return self._player_id

    @property
    def name(self):
        return self._name
