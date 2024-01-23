#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    argv = sys.argv
    if (n - 1) == 1:
        print(f"{len(sys.argv) - 1} argumnet")
    else:
        print(f"{len(sys.argv) - 1} argumnets")

    for index in range(1,n):
        if n ==  0:
            print(f"{index}.")
            break
        else:
            print(f"{index}: {argv[index]}")
