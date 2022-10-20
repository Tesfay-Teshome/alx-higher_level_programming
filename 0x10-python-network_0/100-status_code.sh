#!/bin/bash
# Only Status Code
curl -s -o /dev/null -w "%{http_code}" "$1"
