import time
import os
from datetime import datetime, timedelta
from pathlib import Path
import csv

from influxdb import InfluxDBClient

influx_host = os.getenv("INFLUX_HOST", "localhost")
influx_client = InfluxDBClient(host=influx_host, database="multi-sense")

write_time_interval = 60
start_time = datetime.utcnow()
begin = start_time - timedelta(seconds=100)
end = begin + timedelta(seconds=write_time_interval)

csv_folder_path = os.getenv("CSV_FOLDER_PATH", "./data")
data_folder = Path(csv_folder_path)
data_folder.mkdir(parents=True, exist_ok=True)

while True:
    begin += timedelta(seconds=write_time_interval)
    end += timedelta(seconds=write_time_interval)
    query = 'select * from "bme280" where time > \'' + begin.isoformat() + "Z' AND time <= '" + end.isoformat() + "Z' tz('Europe/Paris')"
    result = influx_client.query(query, epoch="ms")

    try:
        n = next(result.get_points())
    except StopIteration:
        print('Influxdb result query is empty')
    else:
        file_date = datetime.now().strftime('%Y_%m_%d_%H_%M')
        file_name = data_folder/str('bme280_' + file_date + '.csv')
        with file_name.open('a') as csvfile:
            fieldnames = list(next(result.get_points()).keys())
            writer = csv.DictWriter(csvfile, fieldnames)
            if file_name.stat().st_size == 0:
                writer.writeheader()
            for row in result.get_points():
                # query timestamp from influxdb in ms precision
                row['time'] /= 1000.0
                writer.writerow(row)

    time.sleep(write_time_interval - (time.time() - start_time.timestamp()) % write_time_interval)
