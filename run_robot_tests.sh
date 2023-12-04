#!/bin/bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432

psql postgresql://postgres:postgres@localhost:5432 < schema.sql

poetry invoke flask &

poetry run robot src/tests

status=$?
apt-get install lsof
kill $(lsof -t -i:5000)

exit $status