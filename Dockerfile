FROM nginxinc/nginx-unprivileged:1.21.6
USER 10001

# Copy files necessary to compile mibs
COPY poetry.lock pyproject.toml /tmp/
COPY index.py /tmp/new_mibs/index.py
COPY Makefile /tmp/new_mibs/Makefile
COPY scripts /tmp/new_mibs/scripts
COPY output /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY local_mibs.sh /tmp/local_mibs.sh

# Install necassary dependecies
USER root
RUN apt update
RUN apt install -y parallel
RUN apt install -y python3-pip
RUN pip install poetry

# Create directory for poetry's virtual environment
# if not provided - it's being created in the root directory
# what causes problems with permissions
RUN mkdir -p /tmp/.cache
RUN poetry config virtualenvs.path /tmp/.cache
WORKDIR /tmp

# adjust permissions for k8s user
RUN poetry install
RUN chmod a+x /tmp/local_mibs.sh
RUN chown -R 10001:10001 /usr/share/nginx/html
RUN chown -R 10001:10001 /tmp
ENTRYPOINT /tmp/local_mibs.sh && nginx -g 'daemon off;'
