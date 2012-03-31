import unittest

class lifo_n:
    def __init__(self, n=10):
        self.array = [None] * n
        self.index = 0
        self.size = n
    
    def push(self, item):
        if self.index < self.size:
            self.array[self.index] = item
            self.index += 1

        else:
            print "stack full"

    def pop(self):
        if self.index != 0:
            item = self.array[self.index]
            self.index -= 1
            return item
        else:
            print "pop from an empty stack"

    def top(self):
        if self.index != 0:
            return self.array[0]
        else:
            print "pop from an empty stack"

    def length(self):
        return self.index

