#!/usr/bin/env bash

CONTAINER="camera_simulator";
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"  
PACKAGE_DIR="$(dirname "$DIR")/package";

# check if docker is installed and running
if ! [[ $(which docker) && $(docker --version) ]]; then
    echo "Docker is not running"
    exit
fi

if [ "$1" == "down" ]; then
  if [ $( docker ps -a | grep $CONTAINER | wc -l ) -gt 0 ]; then
    docker container stop $CONTAINER && \
    docker container rm $CONTAINER && \
    echo "The container $CONTAINER shut down.";
  else
    echo "The container $CONTAINER doesn't exit."
  fi
else  
  cd "$DIR";

  # build image 
  if [[ "$(docker images -q $CONTAINER 2> /dev/null)" == "" ]]; then
    docker build -t $CONTAINER .;
  fi

  # check if container exists
  if ! [ $( docker ps -a | grep $CONTAINER | wc -l ) -gt 0 ]; then
    docker run --name $CONTAINER -d -v "$PACKAGE_DIR":/home/papp $CONTAINER && \
    docker exec $CONTAINER /bin/sh -c "pip install .";
  fi

  clear;
  echo "Running tests ..."
  docker exec $CONTAINER /bin/sh -c "python -m pytest";
fi