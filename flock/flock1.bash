#!/bin/bash

# This script can be run multiple times simultanously. It creates a
# "sleep" process and locks it using flock. Because we use "flock -n",
# anyone who attempts to rerun while the sleep is still going will
# immediately exit. If you run this many times in a row while
# executing a "ps aux | grep sleep" you will notice that the PID of
# the sleep process doesn't change

(
    # A process will attempt to aquire an exclusive lock here (-x). If
    # the lock cannot be immediately acquired, flock will exit with a
    # non-zero return code (-n). If the lock cannot be acquired, the
    # "exit 1" will be executed - note that this exits from the
    # subprocess (between the parentheses) so the "echo" line at the
    # end will be executed no matter what!
    flock -x -n 200 || { echo "Could not acquire lock"; exit 1; }
    echo "Lock Acquired"

    # If we get here, then the exclusive lock was acquired
    sleep 60

    # At this point, the lock will be held as long as the sleep
    # process is running.
) 200>myfile.lock &

# This is executed whether or not the lock was acquired, every run of
# this script should say HELLO!
echo "HELLO!"
