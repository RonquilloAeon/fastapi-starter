# Multi-stage build to reduce image size
# See https://pythonspeed.com/articles/multi-stage-docker-python/
FROM pypy:3.6-7.1-slim as build

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential python-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip3 install --no-cache-dir --no-warn-script-location --user -r requirements.txt

FROM pypy:3.6-7.1-slim as release

COPY --from=build /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

WORKDIR /app
COPY src ./

EXPOSE 8000

# https://americanexpress.io/do-not-run-dockerized-applications-as-root/
# TODO figure out how to get gunicorn to work when user is set (since gunicorn is installed in /root/.local)
#USER 9000

ENTRYPOINT ["/app/start.sh"]
