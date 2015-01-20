n = 0
coll = []
low = 0

while low < 10:
    n += 1
    low = int((10 ** (n - 1)) ** (1./n) - 0.0001) + 1
    high = int((10 ** n) ** (1./n) + 0.0001)
    for x in xrange(low, high):
        l = len(str(x ** n))
        if l == n:
            coll.append(x)

print len(coll)

