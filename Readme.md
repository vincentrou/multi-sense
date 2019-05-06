Faire soit l'installation Docker (conseillé) soit l'installation Manuelle :

# Docker

* ## Installation

### Docker

https://docs.docker.com/install/linux/docker-ce/ubuntu/

### Docker compose

https://docs.docker.com/compose/install/

* ## Use the code

`docker-compose build`

`docker-compose up`

# Connect to Grafana

`http://localhost:3000`

* user : admin
* pwd : admin
* Ajouter une source de donnée influxdb avec comme nom de base de donnée "multi-sense"
* Ajouter un graphique pour afficher les données dans le temps