#!/bin/bash

if [ "$1" = "start" ]; then
    cd 
    cd Documents/Programming/Github/Assistant/src/
    python3 session.py
else
    cd 
    cd Documents/Programming/Github/Assistant/src/
    echo "$1" > ./assets/question.txt
    python3 question.py
fi