from fifo import FIFO

S = FIFO()
for i in xrange(3):
    S.push(i)

while len(S) > 0: print S.pop(),
print 

try:
    print S.pop()
except IndexError, msg:
    print msg

