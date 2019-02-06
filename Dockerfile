FROM python:3

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "/usr/src/app/cpu_influx.py"]