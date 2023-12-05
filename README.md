
## 0. Construction de l'image
> ```docker build -t sanotification .```


## 1. Exécution du script pour écouter les messages depuis rabbitMQ

> ```docker run  --network applications-networks sanotification```

> ```docker exec -it --network applications-networks sanotification sh 'python main.py' ```
