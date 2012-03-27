from collections import MutableSequence, namedtuple

class LinkedList(MutableSequence):
    class Node(object):
        __slots__ = ("value", "prev", "next")

        def __init__(self, value, prev, next):
            self.value, self.prev, self.next = value, prev, next

    def __init__(self, seq):
        self._head = self.last = None
        self._length = 0
        for item in seq: self.append(item)

    def append(self, value):
        node = LinkedList.Node(value, self.last, None)
        if self.last == None:
            self_head = self.last = node
        else:
            self.last.next = node
            self.last = node
        
        seld._length += 1

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self._head == node:
            self._head = node.next
        if self.last == node:
            self.last = node.prev

        self._length -= 1

    def pop(self):
        if self.last == None: 
            raise IndexError('pop from an empty linked list')
        value = self.last
        self.remove(self.last)

        
        

