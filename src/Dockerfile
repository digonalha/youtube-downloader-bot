FROM python:3.8-slim-buster
ADD . /app
WORKDIR /app

RUN apt-get update && \
    yes | apt-get install --reinstall build-essential && \
    yes | apt-get install libpq-dev gcc  && \
    python3 -m pip install -r requirements.txt && \
    python3 -m pip install -U yt-dlp

CMD [ "python", "./main.py" ]