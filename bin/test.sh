#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

readonly SCRIPT_DIR="$(cd "$(dirname "$0")"; pwd)"
readonly PROJECT_HOME="${SCRIPT_DIR}/.."
readonly SRC_DIR="${PROJECT_HOME}/janken"

cd "${PROJECT_HOME}"

# Static Checking
python -m pycodestyle "${SRC_DIR}"
cd "${SRC_DIR}"
python -m mypy --explicit-package-bases --namespace-packages .
cd -

# Unit Testing
PYTHONPATH="${SRC_DIR}" python -m pytest

# Integration Testing
echo -e "0\n0" | python "${SRC_DIR}/janken_cli_application.py"

# Result
set +o xtrace
GREEN='\e[0;32m'
WRITE='\e[0;37m'
echo -en "${GREEN}"
echo '=============='
echo 'TEST PASSED!!!'
echo '=============='
echo -en "${WRITE}"
set -o xtrace
