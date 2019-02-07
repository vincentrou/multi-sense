import time
import os
import psutil
from influxdb import InfluxDBClient

influx_host = os.getenv('INFLUX_HOST', 'localhost')
influx_client = InfluxDBClient(host=influx_host, database='cpu-sense')
influx_client.create_database('cpu-sense')

while True:
    measurement = [
        {
            'measurement': 'CPU Usage',
            'fields': {
                'value': float(psutil.cpu_percent(0))
            }
        }
    ]
    influx_client.write_points(measurement)
    time.sleep(1)