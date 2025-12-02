#!/bin/bash
# Watchdog for containers
# 

log() {
    echo "$1" | tee -a /var/log/my_docker_rebuild.log
}

rebuild() {
    log "Rebuilding image and container"

    docker build -f Dockerfile -t my_image .
    docker rm -f my_container 2>/dev/null
    docker run --user root -d -p 8080:80 --name my_container my_image
}

is_container_running() {
    docker inspect -f '{{.State.Running}}' my_container 2>/dev/null | grep -q true
}

HASH_FILE="/tmp/last_docker_hash"
CURRENT_HASH=$(sha1sum Dockerfile | awk '{print $1}')

# Create hash file if it do not exists
if [ ! -f "$HASH_FILE" ]; then
    echo "$CURRENT_HASH" > "$HASH_FILE"
    rebuild
    exit 0
fi

OLD_HASH=$(cat "$HASH_FILE")

if [ "$CURRENT_HASH" != "$OLD_HASH" ]; then
    echo "$CURRENT_HASH" > "$HASH_FILE"
    rebuild
else
    # Check if container is running
    if is_container_running; then
        log "Dockerfile unchanged. Container is running."
    else
        log "Dockerfile unchanged. Container is NOT running, Restarting container"
	docker rm -f my_container 2>/dev/null
        docker run --user root -d -p 8080:80 --name my_container my_image
    fi
fi
