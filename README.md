## Prérequis pour tester rabbitmq et le projet sentiment analysis

---

### Démarrer le container

---

- Créer le réseau pour les containers `docker network create applications-networks-simple`
- Construire l'image docker `docker build -t sanotification .`
- Lancer le serveur avec la commande `docker run -it --network [DOCKER_NETWORK] sanotification sh -c "python main.py [ARGS]"` où les détails `[ARGS]` sont :

### Listes des arguments "[ARGS]" disponibles

> -u [USERNAME] : Nom d'utilisateur (Non requis - par défaut 'guest')
> 
> -p [PASSWORD] : Mot de passe (Non requis - par défaut 'guest')
> 
> -rp [RABBITMQ_PORT] : Port du cluster rabbitmq  (Non requis - par défaut 5672)
> 
> -rh [RABBITMQ_HOST] : Host du cluster rabbitmq (Requis)
> 
> -f [QUEUE_NOT_DURABLE] : Si définie, implique que la queue n'est pas 'durable'
> 
> -q [QUEUE_IS_QUORUM] : Si définie, implique que la queue est de type 'quorum'
> 
> -n [QUEUE_NAME] : Nom de la queue (Requis)
