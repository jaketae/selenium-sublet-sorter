#!/bin/bash

pip3 install pipenv
pipenv install -r requirements.txt
pipenv run python main.py --driver_path=$1