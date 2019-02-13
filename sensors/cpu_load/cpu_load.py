import time
import os
import psutil
from influxdb import InfluxDBClient

influx_host = os.getenv('INFLUX_HOST', 'localhost')
influx_dbname = os.getenv('INFLUX_DBNAME', 'multi-sense')
influx_client = InfluxDBClient(host=influx_host, database=influx_dbname)
influx_client.create_database(influx_dbname)

while True:
    measurement = [
        {
            'measurement': 'cpu_load',
            'fields': {
                'value': float(psutil.cpu_percent(0))
            }
        }
    ]
    influx_client.write_points(measurement)
    time.sleep(1)

