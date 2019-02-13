import time
import os
import smbus2
import bme280
from influxdb import InfluxDBClient

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
            'measurement': 'temperature',
            'fields': {
                'value': data.temperature
            },
            'measurement': 'pressure',
            'fields': {
                'value': data.pressure
            },
            'measurement': 'humidity',
            'fields': {
                'value': data.humidity
            }
        }
    ]
    influx_client.write_points(measurement)
    time.sleep(1)

