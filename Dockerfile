FROM python:3.9

ADD ./requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt

ADD ./src /code
WORKDIR /code

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
