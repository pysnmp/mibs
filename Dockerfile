FROM nginxinc/nginx-unprivileged:1.29.1-bookworm
USER 10001

# Copy files necessary to compile mibs
COPY poetry.lock pyproject.toml /app/
COPY index.py /app/new_mibs/index.py
COPY Makefile /app/new_mibs/Makefile
COPY scripts /app/new_mibs/scripts
COPY output /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY local_mibs.sh /app/local_mibs.sh

# Install necassary dependecies
USER root
RUN chmod 644 /etc/nginx/nginx.conf
RUN apt update
RUN apt install -y parallel
RUN apt install -y python3-pip
RUN apt-get update && apt-get install -y --no-install-recommends pipx
ENV PIPX_HOME=/opt/pipx \
    PIPX_BIN_DIR=/usr/local/bin
RUN pipx install 'poetry>=2.1,<3' \
 && chmod -R a+rX /opt/pipx

# Create directory for poetry's virtual environment
# if not provided - it's being created in the root directory
# what causes problems with permissions
RUN mkdir -p /app/.cache
RUN poetry config virtualenvs.path /app/.cache
WORKDIR /app

# adjust permissions for k8s user
RUN poetry install
RUN chmod a+x /app/local_mibs.sh
RUN chown -R 10001:10001 /usr/share/nginx/html
RUN chown -R 10001:10001 /app
USER 10001
ENTRYPOINT /app/local_mibs.sh && nginx -g 'daemon off;'
