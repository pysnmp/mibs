# The corpus, as an image that holds nothing else.
#
# FROM scratch: no base, no shell, no package manager, nothing to patch and
# nothing with a CVE feed. The image is the build host's output directory and
# stops there, which is what lets it be mounted rather than run --
# Kubernetes 1.33 serves an OCI image as a read-only volume, so a pod gets the
# corpus without this repository owning the image that serves it.
#
# Built from output/ or output-compact/ by naming the directory:
#
#   docker build -f docker/corpus.Dockerfile --build-arg CORPUS=output .
#   docker build -f docker/corpus.Dockerfile --build-arg CORPUS=output-compact .
#
# There is deliberately no compile step here. Whatever CORPUS names was built
# by `make corpus`, which is one mibcorpus invocation, and copying it is all
# this file does -- so the image cannot disagree with what CI tested.
FROM scratch

ARG CORPUS=output

# --chmod, because the image states what its contents are readable as rather
# than inheriting it from whatever built the tree. It is mounted into a pod and
# read by nginx running as a uid that has nothing to do with the build host, so
# a mode that came from the builder's umask -- or from tempfile.mkstemp, which
# is 0600 and is what pysmi 3.0.0rc7 leaves behind (pysnmp/pysmi#227) -- is a
# 403 for every module in the tree.
#
# 0755 rather than 0644: the same flag sets directories, and a directory
# nothing may traverse is the same failure one level up. Nothing here is
# executed; it is read over HTTP or opened by a compiler.
COPY --chmod=0755 ${CORPUS}/ /
