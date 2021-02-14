#!/bin/bash
docker build -t mhworth/carta-work-tests .
docker login
docker push mhworth/carta-work-tests
