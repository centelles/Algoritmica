from collections import deque

class FIFO(deque):
    push = deque.append
    enqueue = deque.append

    pop = deque.popleft
    dequeue = deque.popleft

