#!/usr/bin/env bash
# finds the api process so it can be turned off
ps -ef | grep "sudo nohup python3 -m api.v1.app" | grep -v grep
