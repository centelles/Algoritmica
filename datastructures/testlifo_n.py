from lifo_n import lifo_n

s = lifo_n()

print s.length()

for i in xrange(3): s.push(i+1)

print s.length()
print s.top()

while s.length() > 0 : print s.pop(),
print

print s.pop()



