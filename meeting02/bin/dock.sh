#!/bin/bash
IP=`hostname -i`
NAME=$1
if test $NAME
then
  echo
  if docker run -d -it -v /opt/fwac:/opt/fwac -e NAME=$NAME --add-host="fwac:$IP" --add-host="pypi.local:$IP" --name=$NAME lab &> /tmp/$NAME
  then
    echo "Created new container named $NAME"
  elif docker start $NAME &>> /tmp/$NAME
  then
    echo "Using existing container $NAME"
  else
    echo "Assuming $NAME is already running"
  fi
  sleep 2
  echo
  if ! docker exec -it $NAME /bin/bash 
  then
    echo "I didn't make it into the container :("
    echo "You're on your own now"
  fi
  echo
else
  echo "$0 container_name"
fi