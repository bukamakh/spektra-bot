FROM python:2.7-slim
ADD . /src
WORKDIR /src
RUN apt-get update && apt-get -y install gcc && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
CMD python ./bot/app.py
