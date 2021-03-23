#!/usr/bin/env bash
# starts our api
sudo nohup python3 -m api.v1.app > log.txt 2>&1 &
