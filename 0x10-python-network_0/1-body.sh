#!/bin/bash
# script displays the body of the response
curl -L -s -w "%{http_code}" "$1"
