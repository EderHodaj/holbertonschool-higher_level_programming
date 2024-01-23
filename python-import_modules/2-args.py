#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print(f"{len(sys.argv) - 1} argumnets")
    n = len(sys.argv)
    argv = sys.argv
    for index in range(1, n):
        if argv[index]:
            print(f"{index}: {argv[index]}")
        else:
            print(f"{index}.")
