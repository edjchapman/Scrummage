FROM nginx:1.14.2
RUN apt update && apt-get -y install vim htop
ARG NGINX_SERVER_NAME=${NGINX_SERVER_NAME}
COPY proxy.nginx /etc/nginx/nginx.conf
RUN find /etc/nginx/nginx.conf -type f -exec sed -i "s/SERVER_NAME_PLACEHOLDER/${NGINX_SERVER_NAME}/g" {} +
