#!/bin/sh -e

# Get shared-modules, if not there
git submodule update --init --recursive

# You could set DOCKER env to use alternative command like podman
DOCKER=${DOCKER:-docker}

# Build the image
$DOCKER build -t taoky/flatpak-builds .

# Run the container to build bundles
$DOCKER run --rm --cap-add CAP_SYS_ADMIN --cap-add CAP_NET_ADMIN \
  --security-opt seccomp=unconfined --security-opt apparmor=unconfined \
  --device /dev/fuse --network=host \
  -v $(pwd):/workspace taoky/flatpak-builds /workspace/build.py
