#!/bin/bash

exec gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0 "$@"
