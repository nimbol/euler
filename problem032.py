import itertools

digits = '123456789'
p = dict()

# form permutations of digits, size 1, 2, ..., len(pool) using itertools
# from the remaining digits in the pool form a big enough number to get a result with enough digits

for n in xrange(1, 4):
    p['a'] = (''.join(i) for i in itertools.permutations(digits, n))
    for a in p['a']:
        pool = list(digits)
        for d in str(a):
            pool.remove(d)
        p['b'] = (''.join(i) for i in itertools.permutations(pool, m))
        for b in p['b']:
            pass
