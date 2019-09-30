#!/bin/bash

exec gunicorn -w 2 -k uvicorn.workers.UvicornH11Worker main:app -b 0.0.0.0 "$@"
