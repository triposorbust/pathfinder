class Graph():
    """Lightweight graph representation class."""
    def __init__(self, size):
        self._graph = []
        for _ in xrange(size):
            self._graph.append([])
        self.count = size
    def add(self, s, d, w):
        assert(0 <= s < self.count and 0 <= d < self.count)
        self._graph[s].append((d,w))
    def adjacent(self, v):
        assert(0 <= v < self.count)
        return [(u,w) for (u,w) in self._graph[v]]
