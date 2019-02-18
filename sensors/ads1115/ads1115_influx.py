import time
import os
import ADS1115 as ads1115_lib
from influxdb import InfluxDBClient

influx_host = os.getenv('INFLUX_HOST', 'localhost')
influx_dbname = os.getenv('INFLUX_DBNAME', 'multi-sense')
influx_client = InfluxDBClient(host=influx_host, database=influx_dbname)
influx_client.create_database(influx_dbname)

adc = ads1115_lib.ADS1115()

# Add timestamp to measurement
# Accumulate measurement to write multiples points

while True:
    measurement = [
        {
            'measurement': 'ads1115',
            'fields': {
                'ain0': adc.readADCSingleEnded(),
                'ain1': adc.readADCSingleEnded(1),
                'ain2': adc.readADCSingleEnded(channel=2, sps=16),
                'ain3': adc.readADCSingleEnded(channel=3, pga=1024, sps=16)
            }
        }
    ]
    influx_client.write_points(measurement)
    time.sleep(1)

