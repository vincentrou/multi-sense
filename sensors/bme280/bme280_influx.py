import time
import os
import smbus2
import bme280
from influxdb import InfluxDBClient
from random import uniform

# Start sensors at different time after
time.sleep(uniform(10,60))

influx_host = os.getenv('INFLUX_HOST', 'localhost')
influx_dbname = os.getenv('INFLUX_DBNAME', 'multi-sense')
influx_client = InfluxDBClient(host=influx_host, database=influx_dbname)
influx_client.create_database(influx_dbname)

port = 1
address = 0x76
bus = smbus2.SMBus(port)
compensation_params = bme280.load_calibration_params(bus, address)

while True:
    data = bme280.sample(bus, address)
    measurement = [
        {
            'measurement': 'bme280',
            'fields': {
                'temperature': data.temperature,
                'pressure': data.pressure,
                'humidity': data.humidity
            }
        }
    ]
    influx_client.write_points(measurement)
    time.sleep(10)

