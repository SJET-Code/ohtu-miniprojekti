#!/bin/bash

poetry run python3 src/flask_app.py &


poetry run robot src/tests

status=$?
apt-get install lsof
kill $(lsof -t -i:5000)

exit $status