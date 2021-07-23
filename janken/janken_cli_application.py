import csv
from datetime import datetime

from models.hand import Hand
from models.result import Result
from models.player import Player
from models.janken import Janken
from models.janken_detail import JankenDetail
from views.cli.standard_output_view import StandardOutputView

PLAYER_ID_1 = 1
PLAYER_ID_2 = 2

SCAN_PROMPT_VIEW_TEMPLATE = 'scan_prompt.j2'
INVALID_INPUT_VIEW_TEMPLATE = 'invalid_input.j2'
SHOW_HAND_VIEW_TEMPLATE = 'show_hand.j2'
RESULT_VIEW_TEMPLATE = 'result.j2'

DATA_DIR = 'data/'
PLAYERS_CSV = DATA_DIR + 'players.csv'
JANKENS_CSV = DATA_DIR + 'jankens.csv'
JANKEN_DETAILS_CSV = DATA_DIR + 'janken_details.csv'


def find_player_by_id(player_id):
    with open(PLAYERS_CSV) as f:
        reader = csv.reader(f)
        for row in reader:
            player = Player(int(row[0]), row[1])
            if player.player_id == player_id:
                return player
    raise ValueError(f'Player not exist. player_id = {player_id}')


def scan_hand(player):
    while True:
        StandardOutputView(
            SCAN_PROMPT_VIEW_TEMPLATE, {
                'player': player, 'Hand': Hand}).show()
        input_str = input('')
        if input_str in map(lambda h: str(h.value), Hand):
            return Hand(int(input_str))
        else:
            StandardOutputView(
                INVALID_INPUT_VIEW_TEMPLATE, {
                    'input': input_str}).show()


def show_hand_with_name(hand, player):
    params = {
        'hand': hand,
        'player': player
    }
    StandardOutputView("show_hand.j2", params).show()


def create_file_if_not_exist(file_name):
    with open(file_name, 'a'):
        pass


def count_file_lines(file_name):
    with open(file_name) as f:
        return len(f.readlines())


def janken_detail_to_csv_row(janken_detail):
    return [
        janken_detail.janken_detail_id,
        janken_detail.janken_id,
        janken_detail.player_id,
        janken_detail.hand.value,
        janken_detail.result.value,
    ]


def main():

    # プレイヤー名を取得

    player_1 = find_player_by_id(PLAYER_ID_1)
    player_2 = find_player_by_id(PLAYER_ID_2)

    # プレイヤーの手を取得

    player_1_hand = scan_hand(player_1)
    player_2_hand = scan_hand(player_2)

    show_hand_with_name(player_1_hand, player_1)
    show_hand_with_name(player_2_hand, player_2)

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

    # 結果を保存

    create_file_if_not_exist(JANKENS_CSV)

    janken_id = count_file_lines(JANKENS_CSV) + 1
    janken = Janken(janken_id, played_at=datetime.now())

    with open(JANKENS_CSV, 'a') as f:
        writer = csv.writer(f)
        row = [
            janken.janken_id,
            janken.played_at.strftime('%Y/%m/%d %H:%M:%S')
        ]
        writer.writerow(row)

    create_file_if_not_exist(JANKEN_DETAILS_CSV)

    janken_details_count = count_file_lines(JANKEN_DETAILS_CSV)
    janken_detail_1 = JankenDetail(
        janken_details_count + 1,
        janken_id,
        PLAYER_ID_1,
        player_1_hand,
        player_1_result)
    janken_detail_2 = JankenDetail(
        janken_details_count + 2,
        janken_id,
        PLAYER_ID_2,
        player_2_hand,
        player_2_result)
    janken_details = [janken_detail_1, janken_detail_2]

    with open(JANKEN_DETAILS_CSV, 'a') as f:
        writer = csv.writer(f)
        rows = map(janken_detail_to_csv_row, janken_details)
        writer.writerows(rows)

    # 勝敗の表示

    if (player_1_result == Result.WIN):
        winner = player_1
    elif (player_2_result == Result.WIN):
        winner = player_2
    else:
        winner = None

    StandardOutputView(RESULT_VIEW_TEMPLATE, {'winner': winner}).show()


if __name__ == '__main__':
    main()
