import time
import psutil
from influxdb import InfluxDBClient

influx_client = InfluxDBClient('localhost', 8086, database='cpu-sense')
influx_client.create_database('cpu-sense')

f = open('/sys/class/thermal/thermal_zone0/temp', 'r')

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