from models.hand import Hand
from models.player import Player
from services.janken_service import JankenService
from services.player_service import PlayerService
from views.cli.standard_output_view import StandardOutputView

PLAYER_ID_1 = 1
PLAYER_ID_2 = 2

SCAN_PROMPT_VIEW_TEMPLATE = 'scan_prompt.j2'
INVALID_INPUT_VIEW_TEMPLATE = 'invalid_input.j2'
SHOW_HAND_VIEW_TEMPLATE = 'show_hand.j2'
RESULT_VIEW_TEMPLATE = 'result.j2'

PLAYER_NOT_FOUND_ERROR_MESSAGE_FORMAT = 'Player not found. player_id = {}'


class JankenCliController:
    def __init__(
            self,
            player_service: PlayerService,
            janken_service: JankenService):
        self.player_service = player_service
        self.janken_service = janken_service

    def play(self) -> None:

        player_1 = self.player_service.find_player_by_id(PLAYER_ID_1)
        if player_1 is None:
            raise ValueError(
                PLAYER_NOT_FOUND_ERROR_MESSAGE_FORMAT.format(PLAYER_ID_1))
        player_2 = self.player_service.find_player_by_id(PLAYER_ID_2)
        if player_2 is None:
            raise ValueError(
                PLAYER_NOT_FOUND_ERROR_MESSAGE_FORMAT.format(PLAYER_ID_2))

        player_1_hand = self._scan_hand(player_1)
        player_2_hand = self._scan_hand(player_2)

        self._show_hand_with_name(player_1_hand, player_1)
        self._show_hand_with_name(player_2_hand, player_2)

        maybe_winner = self.janken_service.play(
            player_1, player_1_hand, player_2, player_2_hand)

        StandardOutputView(
            RESULT_VIEW_TEMPLATE, {
                'winner': maybe_winner}).show()

    def _scan_hand(self, player: Player) -> Hand:
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

    def _show_hand_with_name(self, hand: Hand, player: Player) -> None:
        params = {
            'hand': hand,
            'player': player
        }
        StandardOutputView("show_hand.j2", params).show()
