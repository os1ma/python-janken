import csv
from datetime import datetime
from typing import Optional, List

from models.hand import Hand
from models.result import Result
from models.player import Player
from models.janken import Janken
from models.janken_detail import JankenDetail
from services.player_service import PlayerService

DATA_DIR = 'data/'
JANKENS_CSV = DATA_DIR + 'jankens.csv'
JANKEN_DETAILS_CSV = DATA_DIR + 'janken_details.csv'


class JankenService:
    def play(
            self,
            player_1: Player,
            player_1_hand: Hand,
            player_2: Player,
            player_2_hand: Hand) -> Optional[Player]:

        # 勝敗判定

        if (player_1_hand == Hand.STONE):

            if (player_2_hand == Hand.STONE):
                player_1_result = Result.DRAW
                player_2_result = Result.DRAW
            elif (player_2_hand == Hand.PAPER):
                player_1_result = Result.LOSE
                player_2_result = Result.WIN
            else:
                player_1_result = Result.WIN
                player_2_result = Result.LOSE

        elif (player_1_hand == Hand.PAPER):

            if (player_2_hand == Hand.STONE):
                player_1_result = Result.WIN
                player_2_result = Result.LOSE
            elif (player_2_hand == Hand.PAPER):
                player_1_result = Result.DRAW
                player_2_result = Result.DRAW
            else:
                player_1_result = Result.LOSE
                player_2_result = Result.WIN

        else:

            if (player_2_hand == Hand.STONE):
                player_1_result = Result.LOSE
                player_2_result = Result.WIN
            elif (player_2_hand == Hand.PAPER):
                player_1_result = Result.WIN
                player_2_result = Result.LOSE
            else:
                player_1_result = Result.DRAW
                player_2_result = Result.DRAW

        # じゃんけんを保存

        self._create_file_if_not_exist(JANKENS_CSV)

        janken_id = self._count_file_lines(JANKENS_CSV) + 1
        janken = Janken(janken_id, played_at=datetime.now())

        with open(JANKENS_CSV, 'a') as f:
            writer = csv.writer(f)
            row = [
                janken.janken_id,
                janken.played_at.strftime('%Y/%m/%d %H:%M:%S')
            ]
            writer.writerow(row)

        # じゃんけん明細を保存

        self._create_file_if_not_exist(JANKEN_DETAILS_CSV)

        janken_details_count = self._count_file_lines(JANKEN_DETAILS_CSV)
        janken_detail_1 = JankenDetail(
            janken_details_count + 1,
            janken_id,
            player_1.player_id,
            player_1_hand,
            player_1_result)
        janken_detail_2 = JankenDetail(
            janken_details_count + 2,
            janken_id,
            player_2.player_id,
            player_2_hand,
            player_2_result)
        janken_details = [janken_detail_1, janken_detail_2]

        with open(JANKEN_DETAILS_CSV, 'a') as f:
            writer = csv.writer(f)
            rows = map(self._janken_detail_to_csv_row, janken_details)
            writer.writerows(rows)

        # 勝者を返却

        if (player_1_result == Result.WIN):
            return player_1
        elif (player_2_result == Result.WIN):
            return player_2
        else:
            return None

    def _create_file_if_not_exist(self, file_name: str) -> None:
        with open(file_name, 'a'):
            pass

    def _count_file_lines(self, file_name: str) -> int:
        with open(file_name) as f:
            return len(f.readlines())

    def _janken_detail_to_csv_row(
            self,
            janken_detail: JankenDetail) -> List[str]:
        return [
            str(janken_detail.janken_detail_id),
            str(janken_detail.janken_id),
            str(janken_detail.player_id),
            str(janken_detail.hand.value),
            str(janken_detail.result.value),
        ]
