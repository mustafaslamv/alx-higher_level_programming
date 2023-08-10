#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    itemsNO = len(argv)
    if itemsNO <= 2:
        print(result)
    else:
        for i in range(1, itemsNO):
            result += int(argv[i])
        print(result)
