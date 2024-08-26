# Usa la imagen base de Ubuntu 18.04
FROM ubuntu:18.04

# Actualiza los repositorios e instala los paquetes necesarios
RUN apt-get update && apt-get install -y nginx nano certbot vim cron
COPY  ./cron.log /var/log

EXPOSE 80 443

# Inicia Cron cuando se ejecute el contenedor
#CMD ["nginx", "-g", "daemon off;"]  # Se recomienda cargar este comando en el docker-compose.yaml
CMD cron && tail -f /var/log/cron.log