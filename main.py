#!/usr/bin/env python

from sys import argv,path
path.append("src")
from src.pathfinder.core import Dijkstras
from src.graphy.core import Graph

START = "A"
END = "B"

def assemble(filename):
    """Assembles a graph object from file specification."""
    count = 0
    index = { } # Keys are names, values are graph indices.
    with open(filename, 'r') as f:
        size = int(f.readline().strip())
        G = Graph(size)
        for line in f:
            words = line.split()
            s = index.get(words[0], None)
            d = index.get(words[1], None)
            if s == None:                     # Here we are
                s = index[words[0]] = count   # making sure
                count += 1                    # we use index
            if d == None:                     # that is not
                d = index[words[1]] = count   # yet in the
                count += 1                    # graph.
            w = int(words[2])
            G.add(s,d,w)
    return G,index

def main(filename):
    G, index = assemble(filename)
    name = dict([(v,k) for k,v in index.iteritems()])

    assert(START in index and END in index)
    pi,d = Dijkstras(G, index[START])

    revroute = []
    current = index[END]
    while current != index[START]:  # Backtrack across path
        revroute.append(current)    # to terminal node using
        current = pi[current]       # array previous-vertex.
    else:
        revroute.append(current)                        # And this is
        print(d[index[END]])                            # the desired
        print(" ".join([name[i]                         # output of a
                        for i in reversed(revroute)]))  # nice format.
    return 0

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage:\n% python main.py <input-filename>")
        exit(1)
    main(argv[1])
