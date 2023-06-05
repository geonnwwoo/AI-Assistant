#!/bin/bash

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ "$1" = "start" ]; then
    cd "$script_dir"
    python3 session.py
elif [ "$1" = "set-personality" ]; then
    cd "$script_dir"
    echo "$2" > ./assets/PERSONALITY.txt
elif [ "$1" = "set-apikey" ]; then
    cd "$script_dir"
    echo "$2" > ./assets/API_KEY.txt
else
    cd "$script_dir"
    echo "$1" > ./assets/question.txt
    python3 question.py
fi