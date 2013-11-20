from heapq import heapify,heappush,heappop

class MinQueue(dict):
    """ Dictionary-based priority-queue implementation. Uses `heappq`
        library for heap maintenance. A hybrid 'Priority Dict' type."""

    def __init__(self, *xs, **kws):
        super(MinQueue, self).__init__(*xs, **kws)
        self._reheapify()

    def _reheapify(self):
        self._heap = [(v,k) for k,v in self.iteritems()]
        heapify(self._heap)

    def extract(self):
        heap = self._heap
        v,k = heappop(heap)
        while k not in self or self[k] != v:
            v,k = heappop(heap)
        del self[k]
        return k

    def __setitem__(self, k, v):
        super(MinQueue, self).__setitem__(k,v)
        if len(self._heap) < 2 * len(self):
            heappush(self._heap, (v,k))
        else:
            self._reheapify()

    def update(self, *xs, **kws):
        super(MinQueue, self).update(*xs, **kws)
        self._reheapify()
