FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN python3 -m pip install -r requirements.txt

COPY influx_to_csv.py /usr/src/app
CMD ["python3", "-u", "/usr/src/app/influx_to_csv.py"]