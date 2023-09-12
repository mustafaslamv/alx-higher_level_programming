# 0x0B. Python - Input/Output


open(r"filename","mode",....)

The r makes the string raw

modes:

- Read Only (‘r’)
- Read and Write (‘r+’)
- Write Only (‘w’)
- Write and Read (‘w+’)
- Append Only (‘a’)
- Append and Read (‘a+’)

--------------------------------------------------------

## with statement

### 1) without using with statement
file = open('file_path', 'w')

file.write('hello world !')

file.close()

### 2) using with statement
```
with open('file_path', 'w') as file:

    file.write('hello world !')

```

there is no need to call file.close() when using with statement. The with statement itself ensures proper acquisition and release of resources

--------------------------------------------------------

read() returns the whole file as str
readline() return single line as str
readlines() return all the file lines as list
