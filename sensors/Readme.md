# Créer des nouveaux capteurs

  * Copier le dossier 'cpu_load' et renommer avec le nom du capteur voulu.
  * Modifier le programme .py pour écrire les données du capteur dans influxdb
  * Générer les requirements à la main ou avec 'pipreqs'
  * Mettre à jour le Dockerfile du nouveau capteur
  * Ajouter le capteur dans le docker-compose.yml
    * En donnant accès au capteurs physique via la section 'devices' : https://stackoverflow.com/questions/30059784/docker-access-to-raspberry-pi-gpio-pins
  * Enregistrer un dashboard dans grafana/provisioning/dashboards
