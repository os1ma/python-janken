import csv
import datetime

from hand import Hand
from result import Result

PLAYER_ID_1 = 1
PLAYER_ID_2 = 2

SCAN_PROPMT_MESSAGE_FORMAT = ''.join(
    [f'{hand.name}: {hand.value}\n' for hand in Hand]) \
    + "Please select {} hand:"
INVALID_INPUT_MESSAGE_FORMAT = 'Invalid input: {}\n'
SHOW_HAND_MESSAGE_FORMAT = '{} selected {}'
WINNING_MESSAGE_FORMAT = '{} win !!!'
DRAW_MESSAGE = 'DRAW !!!'

DATA_DIR = 'data/'
PLAYERS_CSV = DATA_DIR + 'players.csv'
JANKENS_CSV = DATA_DIR + 'jankens.csv'
JANKEN_DETAILS_CSV = DATA_DIR + 'janken_details.csv'


def find_player_name_by_id(player_id):
    with open(PLAYERS_CSV) as f:
        reader = csv.reader(f)
        for row in reader:
            id = int(row[0])
            name = row[1]
            if id == player_id:
                return name
    raise ValueError(f'Player not exist. player_id = {player_id}')


def scan_hand(player_name):
    while True:
        print(SCAN_PROPMT_MESSAGE_FORMAT.format(player_name))
        input_str = input('')
        if input_str in map(lambda h: str(h.value), Hand):
            return Hand(int(input_str))
        else:
            print(INVALID_INPUT_MESSAGE_FORMAT.format(input_str))


def show_hand_with_name(hand, player_name):
    print(SHOW_HAND_MESSAGE_FORMAT.format(player_name, hand.name))


def create_file_if_not_exist(file_name):
    with open(file_name, 'a'):
        pass


def count_file_lines(file_name):
    with open(file_name) as f:
        return len(f.readlines())


def main():

    # プレイヤー名を取得

    player_1_name = find_player_name_by_id(PLAYER_ID_1)
    player_2_name = find_player_name_by_id(PLAYER_ID_2)

    # プレイヤーの手を取得

    player_1_hand = scan_hand(player_1_name)
    player_2_hand = scan_hand(player_2_name)

    show_hand_with_name(player_1_hand, player_1_name)
    show_hand_with_name(player_2_hand, player_2_name)

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
    played_at = datetime.datetime.now()
    played_at_str = played_at.strftime('%Y/%m/%d %H:%M:%S')
    with open(JANKENS_CSV, 'a') as f:
        writer = csv.writer(f)
        row = [janken_id, played_at_str]
        writer.writerow(row)

    create_file_if_not_exist(JANKEN_DETAILS_CSV)
    janken_details_count = count_file_lines(JANKEN_DETAILS_CSV)
    with open(JANKEN_DETAILS_CSV, 'a') as f:
        writer = csv.writer(f)
        janken_detail_id_1 = janken_details_count + 1
        janken_detail_id_2 = janken_details_count + 2
        rows = [
            [
                janken_detail_id_1,
                janken_id,
                PLAYER_ID_1,
                player_1_hand.value,
                player_1_result.value
            ],
            [
                janken_detail_id_2,
                janken_id,
                PLAYER_ID_2,
                player_2_hand.value,
                player_2_result.value
            ]
        ]
        writer.writerows(rows)

    # 勝敗の表示

    if (player_1_result == Result.WIN):
        result_message = WINNING_MESSAGE_FORMAT.format(player_1_name)
    elif (player_2_result == Result.WIN):
        result_message = WINNING_MESSAGE_FORMAT.format(player_2_name)
    else:
        result_message = DRAW_MESSAGE

    print(result_message)


if __name__ == '__main__':
    main()
