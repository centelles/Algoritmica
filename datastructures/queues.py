
class IQueue(Sized, Iterable):
    @abstractmethod
    def push(self, item): raise NotImplementedError

    @abstractmethod
    def pop(self): raise NotImplementedError

    @abstractmethod
    def top(self): raise NotImplementedError


class FIFO(IQueue):
    def __init__(self, data, **kw):
        get_factories(self, kw, sequenceFactory=lambsa data: LinkedList(data)
