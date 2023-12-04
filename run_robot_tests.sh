#!/bin/bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432

psql postgresql://postgres:postgres@localhost:5432 < schema.sql

poetry run flask --app src/flask_app.py run &

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000)" != "200" ]];
  do sleep 1;
done

poetry run robot src/tests

status=$?
apt-get install lsof
kill $(lsof -t -i:5000)

exit $status