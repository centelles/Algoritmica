class OffsetArray(list):
    def __init__(self, initList = None, offset = 1):
        if initList == None:
            initList = []
        list.__init__(self, initList)
        self.offset = offset

    def __getitem__(self, i):
        if self.offset <= i: 
            return list.__getitem__(self, i - self.offset)
        raise IndexError, 'OffsetArray index out of range'

    def __setitem__(self, i, item):
        if self.offset <= i:
            list.__setitem__(self, i - self.offset, item)
        else:
            raise IndexError, 'OffsetArray index out of range'

