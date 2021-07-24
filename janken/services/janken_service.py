from datetime import datetime
from typing import Optional

from daos.protocols.janken_dao import JankenDao
from daos.protocols.janken_detail_dao import JankenDetailDao
from models.hand import Hand
from models.janken import Janken
from models.janken_detail import JankenDetail
from models.player import Player
from models.result import Result


class JankenService:
    def __init__(self, janken_dao: JankenDao,
                 janken_detail_dao: JankenDetailDao):
        self._janken_dao = janken_dao
        self._janken_detail_dao = janken_detail_dao

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

        janken_id = self._janken_dao.count() + 1
        janken = Janken(janken_id, played_at=datetime.now())

        self._janken_dao.insert(janken)

        # じゃんけん明細を保存

        janken_details_count = self._janken_detail_dao.count()
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

        self._janken_detail_dao.insert_all(janken_details)

        # 勝者を返却

        if (player_1_result == Result.WIN):
            return player_1
        elif (player_2_result == Result.WIN):
            return player_2
        else:
            return None
