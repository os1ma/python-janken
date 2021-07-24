import csv
from typing import List
from models.janken_detail import JankenDetail
from daos.csv.csv_dao_utils import DATA_DIR, \
    create_file_if_not_exist, count_file_lines

JANKEN_DETAILS_CSV = DATA_DIR + 'janken_details.csv'


class JankenDetailCsvDao:
    def count(self) -> int:
        create_file_if_not_exist(JANKEN_DETAILS_CSV)
        return count_file_lines(JANKEN_DETAILS_CSV)

    def insert_all(self, janken_details: List[JankenDetail]):
        create_file_if_not_exist(JANKEN_DETAILS_CSV)
        with open(JANKEN_DETAILS_CSV, 'a') as f:
            writer = csv.writer(f)
            rows = map(self._janken_detail_to_csv_row, janken_details)
            writer.writerows(rows)

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
