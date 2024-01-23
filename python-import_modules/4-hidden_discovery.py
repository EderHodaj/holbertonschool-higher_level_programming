#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for names in hidden_4:
        if name[0] == "_" and name[1] == "_":
            continue
        else:
            print(sorted(name))
