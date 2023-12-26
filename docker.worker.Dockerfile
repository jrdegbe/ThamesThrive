FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends git && apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:/app:$PATH"

RUN /opt/venv/bin/python3 -m pip install --upgrade pip

RUN mkdir -p app
WORKDIR /app

COPY ThamesThrive/worker/requirements.txt .
RUN pip install wheel
RUN pip --default-timeout=240 install -r requirements.txt

COPY ThamesThrive/worker ./ThamesThrive/worker
WORKDIR /app

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["celery", "-A","ThamesThrive.worker.celery_worker","worker", "-l", "info", "--uid=nobody", "--gid=nogroup"]
