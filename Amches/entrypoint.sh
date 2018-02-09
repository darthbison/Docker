#!/bin/sh

tearDown() {

	echo "Goodbye"
	exit 0
}

trap tearDown 2 1 15
DATE="$(date)"
CONT="$(cat /proc/1/cgroup | grep 'docker/' | tail -1 | sed 's/^.*\///' | cut -c 1-12)"
echo "Container ${CONT} has come online at ${DATE}" >> ContainerID.txt

while true; do
	sleep 3600
done
