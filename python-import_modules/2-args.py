#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    argv = sys.argv
    if (n - 1) == 1:
        print(f"{len(sys.argv) - 1} argumnet")
    elif n == 1:
        print("0 arguments.")
    else:
        print(f"{len(sys.argv) - 1} argumnets")

    for index in range(1, n):
        print(f"{index}: {argv[index]}")
