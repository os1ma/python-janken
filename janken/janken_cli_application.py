from controllers.cli.janken_cli_controller import JankenCliController
from services.player_service import PlayerService
from services.janken_service import JankenService
from daos.csv.player_csv_dao import PlayerCsvDao
from daos.csv.janken_csv_dao import JankenCsvDao
from daos.csv.janken_detail_csv_dao import JankenDetailCsvDao


def main() -> None:
    player_dao = PlayerCsvDao()
    janken_dao = JankenCsvDao()
    janken_detail_dao = JankenDetailCsvDao()

    player_service = PlayerService(player_dao)
    janken_service = JankenService(janken_dao, janken_detail_dao)

    controller = JankenCliController(player_service, janken_service)

    controller.play()


if __name__ == '__main__':
    main()
