FROM pypy:3.6-7.1-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential python-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY src ./

RUN pip3 install -r requirements.txt

EXPOSE 8000

# https://americanexpress.io/do-not-run-dockerized-applications-as-root/
USER 9000

ENTRYPOINT ["/app/start.sh"]
