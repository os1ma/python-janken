#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

readonly SCRIPT_DIR="$(cd "$(dirname "$0")"; pwd)"
readonly PROJECT_HOME="${SCRIPT_DIR}/.."
readonly SRC_DIR="${PROJECT_HOME}/janken"

cd "${PROJECT_HOME}"

python -m pycodestyle "${SRC_DIR}/janken_cli_application.py"

PYTHONPATH="${SRC_DIR}" python -m pytest

echo -e "0\n0" | python "${SRC_DIR}/janken_cli_application.py"
