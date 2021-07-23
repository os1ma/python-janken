# python-janken

[![main](https://github.com/os1ma/python-janken/actions/workflows/main.yaml/badge.svg)](https://github.com/os1ma/python-janken/actions/workflows/main.yaml)

[![schedule](https://github.com/os1ma/python-janken/actions/workflows/schedule.yaml/badge.svg)](https://github.com/os1ma/python-janken/actions/workflows/schedule.yaml)

## Development Dependencies

- asdf

## SetUp

```console
asdf plugin-add python
asdf install
pip install -r requirements.txt
ln -s ../../bin/pre-commit .git/hooks/pre-commit
```

## Development

format

```console
./bin/format.sh
```

test

```console
./bin/test.sh
```

run

```console
python janken/janken_cli_application.py
```
