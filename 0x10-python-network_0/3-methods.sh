#!/bin/bash
# Bash script that displays all HTTP methods the server will accept.
curl -s "$1" -I | awk '/Allow:/{print substr($0, 8, length($0) - 8)}'
