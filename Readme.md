# Installation

## Influxdb

https://docs.influxdata.com/influxdb/v1.7/introduction/installation/

## Grafana

http://docs.grafana.org/installation/debian/

# Use the code

`git clone`

`cd influxdb/sensor`

`python3 -m pip install -r requirements.txt`

`python3 cpu_influx.py`

# Configure Grafana

`http://localhost:3000`

  * Ajouter une source de donnée influxdb avec comme nom de base de donnée "cpu-sense"
  * Ajouter un graphique pour afficher usage CPU dans le temps