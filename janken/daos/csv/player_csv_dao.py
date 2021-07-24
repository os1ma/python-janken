import csv
from typing import Optional

from daos.csv.csv_dao_utils import DATA_DIR
from daos.protocols.player_dao import PlayerDao
from models.player import Player

PLAYERS_CSV = DATA_DIR + 'players.csv'


class PlayerCsvDao(PlayerDao):
    def find_player_by_id(self, player_id: int) -> Optional[Player]:
        with open(PLAYERS_CSV) as f:
            reader = csv.reader(f)
            for row in reader:
                player = Player(int(row[0]), row[1])
                if player.player_id == player_id:
                    return player
            else:
                return None
