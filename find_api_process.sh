#!/usr/bin/env bash
# starts our api
ps -ef | grep "sudo nohup python3 -m api.v1.app" | grep -v grep
