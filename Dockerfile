FROM nginxinc/nginx-unprivileged:1.23.1
COPY output /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf