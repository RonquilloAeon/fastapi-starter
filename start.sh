#!/bin/bash

exec gunicorn -w 2 -k uvicorn.workers.UvicornWorker api:app -b 0.0.0.0 "$@"
