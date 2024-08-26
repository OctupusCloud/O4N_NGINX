# Usa la imagen base de Ubuntu 23.10
FROM ubuntu:23.10

# Actualiza los repositorios e instala los paquetes necesarios
RUN apt update && apt install -y nginx nano certbot vim cron
RUN apt install python3-certbot-nginx
COPY  ./cron.log /var/log

EXPOSE 80 443

# Inicia Cron cuando se ejecute el contenedor
CMD cron && tail -f /var/log/cron.log