#!/bin/bash
docker ps
docker rmi -f example:new
docker build -t example:new .
docker compose up