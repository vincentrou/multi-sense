import time
import os
from datetime import datetime
import threading
import ADS1115 as ads1115_lib
from influxdb import InfluxDBClient

influx_host = os.getenv('INFLUX_HOST', 'localhost')
influx_dbname = os.getenv('INFLUX_DBNAME', 'multi-sense')
influx_client = InfluxDBClient(host=influx_host, database=influx_dbname)
influx_client.create_database(influx_dbname)

adc = ads1115_lib.ADS1115()

# Add timestamp to measurement
# Accumulate measurement to write multiples points
measurement = []

def getMeasurements():
    new_measurement = {
            'measurement': 'ads1115',
            'time': datetime.now(),
            'fields': {
                'ain0': adc.readADCSingleEnded(),
                'ain1': adc.readADCSingleEnded(1),
                'ain2': adc.readADCSingleEnded(channel=2, sps=16),
                'ain3': adc.readADCSingleEnded(channel=3, pga=1024, sps=16)
            }
        }
    measurement.append(new_measurement)

threading.Timer(0.1, getMeasurements).start()

while True:
    influx_client.write_points(measurement)
    measurement.clear()
    time.sleep(1)

