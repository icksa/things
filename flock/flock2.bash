#!/bin/bash

# Here is how you use flock without creating a subshell

lock_file="myfile.lock"

function fail {
    echo "Failed to Acquire Lock (I am $$)"
    exit 1
}

exec 9>${lock_file}
flock -x -n 9 || fail
echo "Process $$ acquired lock"
sleep 10
