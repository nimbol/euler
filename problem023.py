import mymath

limit = 28124
checklist = set(range(1, limit))
abundants = set()
collected = []
cache = set()

try:
    while checklist:
        n = min(checklist)
        checklist.remove(n)
        if sum(mymath.divisors(n)) > 2 * n:
            # store new abundant
            abundants.add(n)
            # multiples of abundants are abundants too
            # they can be written as the sum of two abundants though,
            # so no need to keep them in the checklist
            new_ones = xrange(n, limit, n)
            checklist.difference_update(new_ones)
            abundants.update(new_ones)
        if not any((n - a in abundants) for a in abundants):
            # number can't be written as sum of two abundants
            collected.append(n)
except KeyboardInterrupt:
    print
    print 'n =', n
    print 'remaining todo:', len(checklist), '/', limit
    print 'abundants found:', len(abundants)
    print 'collected', len(collected)

print sum(collected)
