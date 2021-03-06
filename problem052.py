'''
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
'''

d = 3
go = True

while go:
    start = int('1234567890'[:d])
    stop  = int('1666666666'[:d])
    for x in xrange(start, stop):
        coll = set(''.join(sorted(str(x * i))) for i in range(1, 7))
        if len(coll) == 1:
            go = False
            break
    else:
        d += 1

print x
