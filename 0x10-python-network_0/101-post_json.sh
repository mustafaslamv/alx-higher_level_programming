#!/bin/bash
# send json file in POST method
curl -s "$1" -X POST -H "Content-Type: application/json" -d "@$2"
