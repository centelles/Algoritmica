from offsetarray import OffsetArray

a = OffsetArray([10,20,30])
a.append(40)
for i in xrange(1, len(a)+1):
    print (i, a[i]),
print
a[1]=0
print a


