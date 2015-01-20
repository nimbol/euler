from fibonacci import tribonacci
from mymath import divisors

gen = tribonacci()
divs = range(1, 249, 2)

for t in gen:
    # try dividing by all divs up to sqrt(t)
    # discard any divs that evenly divide t
    # append a new div to the list, try dividing all t > newdiv**2
    divs.update(divisors(gen.next()))

print gen.next()

n = 0
i = 1

#while n < 124:
#    i += 2
#    if i not in divs:
#        n += 1
#        print i

print 27 not in divs
