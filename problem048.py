'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

r = 0  # result
for i in xrange(1001):
    r += i ** i
    # truncate r to 10 digits
    r = int(str(r)[-10:])

print r
