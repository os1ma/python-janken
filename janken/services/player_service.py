from typing import Optional
from models.player import Player
from daos.csv.player_csv_dao import PlayerCsvDao


class PlayerService:
    def __init__(self, player_dao: PlayerCsvDao):
        self._player_dao = player_dao

    def find_player_by_id(self, player_id: int) -> Optional[Player]:
        return self._player_dao.find_player_by_id(player_id)
