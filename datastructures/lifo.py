from collections import deque

class LIFO(deque):
    push = deque.append

    def top(self):
        return self[0]

Stack = LIFO

