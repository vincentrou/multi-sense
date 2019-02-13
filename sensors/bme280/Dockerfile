FROM python:3

RUN mkdir -p /usr/src/app
COPY *.py /usr/src/app
COPY requirements.txt /usr/src/app
WORKDIR /usr/src/app

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "/usr/src/app/bme280_influx.py"]
