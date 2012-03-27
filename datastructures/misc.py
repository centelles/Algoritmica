from collections import Container, Iterable, Sized

class RangeSet(Container, Iterable, Sized):

    def __init__(self, min, max):
        self._min, self._max = min, max

    def __contains__(self, v):
        return self._min <= v <= self._max

    def __iter__(self):
        for i in xrange(self._min, self._max + 1):
            yield i

    def __len__(self):
        return self._max - self._min + 1

    def __repr__(self):
        return '{}({!r}, {!r})'.format(self.__class__.__name__, self._min, self._max)


