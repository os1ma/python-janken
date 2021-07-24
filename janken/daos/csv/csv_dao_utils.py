DATA_DIR = 'data/'


def create_file_if_not_exist(file_name: str) -> None:
    with open(file_name, 'a'):
        pass


def count_file_lines(file_name: str) -> int:
    with open(file_name) as f:
        return len(f.readlines())
