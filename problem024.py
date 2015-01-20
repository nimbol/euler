import itertools

g=(''.join(str(j) for j in i) for i in itertools.permutations(range(10), 10))

for i in range(10**6 - 1):
    g.next()

print g.next()
