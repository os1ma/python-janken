import csv
import datetime

PLAYER_ID_1 = 1
PLAYER_ID_2 = 2

STONE_NUM = 0
PAPER_NUM = 1
SCISSORS_NUM = 2

HANDS = {
    'STONE': STONE_NUM,
    'PAPER': PAPER_NUM,
    'SCISSORS': SCISSORS_NUM
}

WIN = 0
LOSE = 1
DRAW = 2

SCAN_PROPMT_MESSAGE_FORMAT = ''.join(
    [f'{hand}: {HANDS[hand]}\n' for hand in HANDS]) + "Please select {} hand:"
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
        if input_str in map(str, HANDS.values()):
            return int(input_str)
        else:
            print(INVALID_INPUT_MESSAGE_FORMAT.format(input_str))


def hand_num_to_str(hand_num):
    for key, value in HANDS.items():
        if value == hand_num:
            return key
    raise ValueError(f'Invalid hand value. hand_num = {hand_num}')


def show_hand_with_name(hand_num, player_name):
    hand_str = hand_num_to_str(hand_num)
    print(SHOW_HAND_MESSAGE_FORMAT.format(player_name, hand_str))


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

    if (player_1_hand == STONE_NUM):

        if (player_2_hand == STONE_NUM):
            player_1_result = DRAW
            player_2_result = DRAW
        elif (player_2_hand == PAPER_NUM):
            player_1_result = LOSE
            player_2_result = WIN
        else:
            player_1_result = WIN
            player_2_result = LOSE

    elif (player_1_hand == PAPER_NUM):

        if (player_2_hand == STONE_NUM):
            player_1_result = WIN
            player_2_result = LOSE
        elif (player_2_hand == PAPER_NUM):
            player_1_result = DRAW
            player_2_result = DRAW
        else:
            player_1_result = LOSE
            player_2_result = WIN

    else:

        if (player_2_hand == STONE_NUM):
            player_1_result = LOSE
            player_2_result = WIN
        elif (player_2_hand == PAPER_NUM):
            player_1_result = WIN
            player_2_result = LOSE
        else:
            player_1_result = DRAW
            player_2_result = DRAW

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
                player_1_hand,
                player_1_result
            ],
            [
                janken_detail_id_2,
                janken_id,
                PLAYER_ID_2,
                player_2_hand,
                player_2_result
            ]
        ]
        writer.writerows(rows)

    # 勝敗の表示

    if (player_1_result == WIN):
        result_message = WINNING_MESSAGE_FORMAT.format(player_1_name)
    elif (player_2_result == WIN):
        result_message = WINNING_MESSAGE_FORMAT.format(player_2_name)
    else:
        result_message = DRAW_MESSAGE

    print(result_message)


if __name__ == '__main__':
    main()
