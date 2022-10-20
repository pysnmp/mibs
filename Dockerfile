FROM nginxinc/nginx-unprivileged:1.23.2
COPY output /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf