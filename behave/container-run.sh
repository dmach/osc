#!/bin/sh

TOPDIR=$(dirname $(readlink -f $0))

podman run \
    --name obs-server \
    --hostname obs-server \
    --replace \
    --detach \
    --interactive \
    --tty \
    --volume="$TOPDIR":/opt/obs \
    --cap-add SYS_PTRACE \
    -p 1443:443 \
    obs-server

sleep 0.5
podman exec -it obs-server /usr/bin/systemctl is-system-running --wait
