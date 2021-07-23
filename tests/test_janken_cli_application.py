from io import StringIO
import textwrap
from janken.janken_cli_application import main

def test_hoge(monkeypatch, capsys):
    player_1_hand = 0
    player_2_hand = 0
    input_str = f'{player_1_hand}\n{player_2_hand}\n'
    monkeypatch.setattr('sys.stdin', StringIO(input_str))

    main()

    expected = textwrap.dedent('''\
    STONE: 0
    PAPER: 1
    SCISSORS: 2
    Please select Alice hand:
    STONE: 0
    PAPER: 1
    SCISSORS: 2
    Please select Bob hand:
    Alice selected STONE
    Bob selected STONE
    DRAW !!!
    ''')
    captured = capsys.readouterr()
    assert captured.out == expected
