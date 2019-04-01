FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN python3 -m pip install -r requirements.txt

COPY ads1115_influx.py /usr/src/app
CMD ["python3", "-u", "/usr/src/app/ads1115_influx.py"]