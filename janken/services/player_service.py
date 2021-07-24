import csv
from models.player import Player

DATA_DIR = 'data/'
PLAYERS_CSV = DATA_DIR + 'players.csv'


class PlayerService:
    def find_player_by_id(self, player_id: int) -> Player:
        with open(PLAYERS_CSV) as f:
            reader = csv.reader(f)
            for row in reader:
                player = Player(int(row[0]), row[1])
                if player.player_id == player_id:
                    return player
        raise ValueError(f'Player not exist. player_id = {player_id}')
