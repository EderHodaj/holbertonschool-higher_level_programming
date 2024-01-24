#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    sentences = dir(hidden_4)
    for name in sentences:
        if name[0] != "_":
            print(name)
