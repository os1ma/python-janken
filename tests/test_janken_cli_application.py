import pytest
import textwrap
from io import StringIO
from janken.janken_cli_application import main

valid_input_test_data = [
    (0, 0, 'STONE', 'STONE', 'DRAW !!!', 2, 2),
    (0, 1, 'STONE', 'PAPER', 'Bob win !!!', 1, 0),
    (0, 2, 'STONE', 'SCISSORS', 'Alice win !!!', 0, 1),
    (1, 0, 'PAPER', 'STONE', 'Alice win !!!', 0, 1),
    (1, 1, 'PAPER', 'PAPER', 'DRAW !!!', 2, 2),
    (1, 2, 'PAPER', 'SCISSORS', 'Bob win !!!', 1, 0),
    (2, 0, 'SCISSORS', 'STONE', 'Bob win !!!', 1, 0),
    (2, 1, 'SCISSORS', 'PAPER', 'Alice win !!!', 0, 1),
    (2, 2, 'SCISSORS', 'SCISSORS', 'DRAW !!!', 2, 2),
]


@pytest.mark.parametrize(
    "player_1_hand_num,player_2_hand_num,player_1_hand_str,player_2_hand_str,result_message,player_1_result,player_2_result",
    valid_input_test_data)
def test_hoge(
        monkeypatch,
        capsys,
        player_1_hand_num,
        player_2_hand_num,
        player_1_hand_str,
        player_2_hand_str,
        result_message,
        player_1_result,
        player_2_result):
    input_str = f'{player_1_hand_num}\n{player_2_hand_num}\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))

    main()

    expected = textwrap.dedent(f'''\
    STONE: 0
    PAPER: 1
    SCISSORS: 2
    Please select Alice hand:
    STONE: 0
    PAPER: 1
    SCISSORS: 2
    Please select Bob hand:
    Alice selected {player_1_hand_str}
    Bob selected {player_2_hand_str}
    {result_message}
    ''')
    captured = capsys.readouterr()
    assert captured.out == expected
