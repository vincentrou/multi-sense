# Docker

* ## Installation

### Docker

https://docs.docker.com/install/linux/docker-ce/ubuntu/

### Docker compose

https://docs.docker.com/compose/install/

* ## Use the code

`docker-compose up`

# Manuellement

* ## Installation

### Influxdb

https://docs.influxdata.com/influxdb/v1.7/introduction/installation/

### Grafana

http://docs.grafana.org/installation/debian/

* ## Use the code

`git clone`

`cd influxdb/sensor`

`python3 -m pip install -r requirements.txt`

`python3 cpu_influx.py`

# Connect to Grafana

`http://localhost:3000`

* user : admin
* pwd : admin
* Ajouter une source de donnée influxdb avec comme nom de base de donnée "cpu-sense"
* Ajouter un graphique pour afficher usage CPU dans le temps