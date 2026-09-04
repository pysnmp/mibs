FROM debian:bookworm-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:0.12.9 /uv /usr/local/bin/uv
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && rm -rf /var/lib/apt/lists/*

ENV UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_PYTHON_PREFERENCE=only-managed \
    UV_PYTHON=3.11 \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

WORKDIR /src
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev


FROM nginxinc/nginx-unprivileged:1.29.1-bookworm

USER root
RUN chown 10001:10001 /usr/share/nginx/html
USER 10001

COPY --from=builder --chown=10001:10001 /opt/python /opt/python
COPY --from=builder --chown=10001:10001 /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH \
    MIBDUMP=mibdump

COPY --chown=0:0 --chmod=644 nginx.conf /etc/nginx/nginx.conf
COPY --chown=10001:10001 --chmod=755 local_mibs.sh mibserver-entrypoint.sh /app/
COPY --chown=10001:10001 index.py /app/new_mibs/index.py
COPY --chown=10001:10001 scripts /app/new_mibs/scripts
COPY --chown=10001:10001 output /usr/share/nginx/html

WORKDIR /app
USER 10001
ENTRYPOINT ["/app/mibserver-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
