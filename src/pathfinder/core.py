from sys import maxint
from graphy.core import Graph
from prioritea.core import MinQueue

def Dijkstras(G,s):
    pi = [None] * G.count
    d = [maxint] * G.count
    d[s] = 0

    S = set()
    Q = MinQueue(zip(xrange(G.count), d))
    while len(Q):
        u = Q.extract()
        S.add(u)
        for v,w in G.adjacent(u):
            if d[v] > d[u] + w:
                Q[v] = d[v] = d[u] + w
                pi[v] = u
    return pi,d
