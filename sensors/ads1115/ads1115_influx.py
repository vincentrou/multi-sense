import time
import os
from datetime import datetime
import threading
import ADS1115 as ads1115_lib
from influxdb import InfluxDBClient
from random import uniform

# Start sensors at different time after
time.sleep(uniform(10,60))

influx_host = os.getenv('INFLUX_HOST', 'localhost')
influx_dbname = os.getenv('INFLUX_DBNAME', 'multi-sense')
influx_client = InfluxDBClient(host=influx_host, database=influx_dbname)
influx_client.create_database(influx_dbname)

adc = ads1115_lib.ADS1115()

# Add timestamp to measurement
# Accumulate measurement to write multiples points
interval = 0.1
measurement = []
measurement_lock = threading.Lock()
start_time = time.time()

def getMeasurements():
    while True:
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
        with measurement_lock:
            measurement.append(new_measurement)
        time.sleep(interval - (time.time() - start_time) % interval)

t = threading.Thread(target=getMeasurements)
t.start()

while True:
    if t.isAlive() == False:
        print("Exiting acquisition thread died")
        exit()
    with measurement_lock:
        influx_client.write_points(measurement)
        measurement.clear()
    time.sleep(10)

t.join()

