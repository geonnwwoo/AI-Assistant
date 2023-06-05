#!/bin/bash

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ "$1" = "start" ]; then
    cd "$script_dir"
    python3 session.py
else
    cd "$script_dir"
    echo "$1" > ./assets/question.txt
    python3 question.py
fi