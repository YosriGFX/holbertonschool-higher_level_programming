#!/bin/bash
# Bash script that  sends a POST request to the passed URL
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
