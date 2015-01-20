import icf

print sum(len(icf.repr(n)[1]) % 2 for n in xrange(10001))
