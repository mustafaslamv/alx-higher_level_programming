#!/usr/bin/python3
output = ''
for value in range(ord('a'), ord('z') + 1):
    output += chr(value)
print(output, end="")
