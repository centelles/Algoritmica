from lifo import Stack

S = Stack()

for i in xrange(3): S.push(i)

print S.top()

while len(S) > 0 : print S.pop(),
print

try:
    print S.pop()
except IndexError, msg:
    print msg

