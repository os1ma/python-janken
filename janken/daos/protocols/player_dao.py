from typing import Optional
from typing import Protocol

from models.player import Player


class PlayerDao(Protocol):
    def find_player_by_id(self, player_id: int) -> Optional[Player]:
        ...
