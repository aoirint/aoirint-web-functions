FROM python:3.9

ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PATH=/home/user/.local/bin:${PATH}

RUN apt-get update && \
    apt-get install -y \
        gosu && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 -o user

ADD ./requirements.txt /
RUN gosu user pip3 install --no-cache-dir -r /requirements.txt

ADD ./src /code
WORKDIR /code

CMD [ "gosu", "user", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
