#!/bin/bash
# return status code of the response
curl -sL "$1" -o /dev/null -w "%{http_code}"
