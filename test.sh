#!/bin/bash

docker build -f DockerfileTest -t addressbooktest .
docker run addressbooktest
