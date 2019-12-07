#!/bin/bash

while !</dev/tcp/db/5432; do
sleep 10
done

exec uvicorn --host 0.0.0.0 --log-level debug api:app "$@"
