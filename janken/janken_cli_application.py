from controllers.cli.janken_cli_controller import JankenCliController
from services.player_service import PlayerService
from services.janken_service import JankenService


def main() -> None:
    player_service = PlayerService()
    janken_service = JankenService()

    controller = JankenCliController(player_service, janken_service)

    controller.play()


if __name__ == '__main__':
    main()
