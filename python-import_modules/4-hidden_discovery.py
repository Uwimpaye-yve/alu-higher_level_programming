#!/usr/bin/python3
import hidden_4

def print_names():
    names = sorted(name for name in dir(hidden_4) if not name.startswith("__"))
    for name in names:
        print(name)

if __name__ == "__main__":
    print_names()
