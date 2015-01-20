import pythagoras, mymath
import time
_t = time.time()


for n in mymath.divisors(1000):
    t = tuple(pythagoras.triplet(n))
    if t:
        break

d = 1000 / n
print d * sum(t[0]), tuple(d * i for i in t[0])

print time.time() - _t
