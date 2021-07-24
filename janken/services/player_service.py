from typing import Optional

from daos.protocols.player_dao import PlayerDao
from models.player import Player


class PlayerService:
    def __init__(self, player_dao: PlayerDao):
        self._player_dao = player_dao

    def find_player_by_id(self, player_id: int) -> Optional[Player]:
        return self._player_dao.find_player_by_id(player_id)
