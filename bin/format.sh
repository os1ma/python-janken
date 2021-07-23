#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

readonly SCRIPT_DIR="$(cd "$(dirname "$0")"; pwd)"
readonly PROJECT_HOME="${SCRIPT_DIR}/.."

find "${PROJECT_HOME}/janken" -type f -name '*.py' \
 | xargs python -m autopep8 --in-place --aggressive --aggressive
