#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    n = len(sys.argv)
    count = 0
    for i in range(1, n):
        count = count + int(arguments[i])
    print(count)
