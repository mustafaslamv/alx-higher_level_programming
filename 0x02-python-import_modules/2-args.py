#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    itemsNO = len(argv)
    if itemsNO == 1:
        print("0 arguments.")
    else:
        if itemsNO == 2:
            print(f"{itemsNO - 1} argument:")
        else:
            print(f"{itemsNO - 1} arguments:")
        for i in range(1, itemsNO):
            print(f"{i:d}: {argv[i]}")
