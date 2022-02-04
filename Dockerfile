FROM nginxinc/nginx-unprivileged:1.21.5
COPY output /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf