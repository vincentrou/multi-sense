FROM python:3

RUN mkdir -p /usr/src/app
COPY cpu_influx.py /usr/src/app
COPY requirements.txt /usr/src/app
WORKDIR /usr/src/app

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "/usr/src/app/cpu_influx.py"]