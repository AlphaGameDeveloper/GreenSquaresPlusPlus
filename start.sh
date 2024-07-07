#!/bin/bash

chmod 600 /root/.ssh/id_*

git config --global user.name "GreenSquares++"
git config --global user.email "null@example.com"

python /docker/greensquares.py
