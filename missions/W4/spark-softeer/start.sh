#!/bin/bash


if [ $1 = "master" ]; then
    LOG_FILE=$(./sbin/start-master.sh | sed "s/.\+logging to //")
    ./sbin/start-connect-server.sh
elif [ $1 = "worker" ]; then
    LOG_FILE=$(./sbin/start-worker.sh spark://master:7077 | sed "s/.\+logging to //")
else
    echo "Usage: $0 [master|worker]"
    exit 1
fi 

tail -f $LOG_FILE