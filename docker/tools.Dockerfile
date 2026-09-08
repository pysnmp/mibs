# pysmi, for the one thing that has to compile a MIB at run time.
#
# charts/mibserver lets a user mount their own MIB sources and have them served
# beside the published corpus, which means compiling them where they are
# mounted. That is the only remaining reason this project ships an image with
# code in it, and this is that image: an upstream Python base and pysmi from
# PyPI, with nothing of ours added.
#
# It is not the serving image. nginx comes from upstream unmodified and the
# corpus arrives as a volume; this runs as an init container, writes what it
# compiled into an emptyDir, and exits.
#
# The compile it runs is `mibcorpus`, the same driver CI builds the published
# corpus with -- so a user's MIBs are compiled by the same code, with the same
# precedence rules, as everything else in the tree they are served beside.
FROM python:3.13-slim

# Exactly the version uv.lock resolves for the corpus build, not a range.
# What this image compiles ends up served beside what that build produced, so
# the two have to be the same compiler: a range lets an image built next month
# put a different pysmi behind the same chart version. tests/chart-contract.sh
# fails if this drifts from the lockfile.
ARG PYSMI_VERSION="3.0.0rc8"

RUN pip install --no-cache-dir "pysnmp-pysmi==${PYSMI_VERSION}" \
 && useradd --uid 10001 --create-home --shell /usr/sbin/nologin mibs

USER 10001
