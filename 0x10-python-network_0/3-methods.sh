#!/bin/bash
# all available methods
curl -sIL "$1" | grep -i 'Allow' | cut -c 8-
