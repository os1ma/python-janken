import csv
from models.janken import Janken
from daos.csv.csv_dao_utils import DATA_DIR, \
    create_file_if_not_exist, count_file_lines

JANKENS_CSV = DATA_DIR + 'jankens.csv'


class JankenCsvDao:
    def count(self) -> int:
        create_file_if_not_exist(JANKENS_CSV)
        return count_file_lines(JANKENS_CSV)

    def insert(self, janken: Janken) -> None:
        create_file_if_not_exist(JANKENS_CSV)
        with open(JANKENS_CSV, 'a') as f:
            writer = csv.writer(f)
            row = [
                janken.janken_id,
                janken.played_at.strftime('%Y/%m/%d %H:%M:%S')
            ]
            writer.writerow(row)
