#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = map(int, argv[1:])
    print(sum(argv))
