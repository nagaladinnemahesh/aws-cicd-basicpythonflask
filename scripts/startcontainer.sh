#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull mahesh0404/python-flask-cicd
# Run the Docker image as a container
docker run -d -p 5000:5000 mahesh0404/python-flask-cicd
