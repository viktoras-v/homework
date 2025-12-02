#!/bin/sh

while true; do
    JOB=$(redis-cli -h redis BRPOP jobs 5 | tail -n1)

    if [ -n "$JOB" ]; then
        echo "Processed job: $JOB"
    fi
done
