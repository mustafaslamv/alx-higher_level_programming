#!/bin/bash
# send json file in POST method
culr -sL "$1" -X POST -H "Content-Type: application/json" -d "@$2"
