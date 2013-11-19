#!/usr/bin/env python

from sys import argv,path
import src.pathfinder.core as pathfinder

def main(filename):
    with open(filename, 'r') as f:
        pass
    return

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage:\n% python main.py <input-filename>")
        exit(1)
    main(argv[1])
