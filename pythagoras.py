def triplet(n):
    for a in xrange(1, n):
        for b in xrange(a, n):
            cc = (a**2 + b**2) ** 0.5
            c = int(cc)
            if c != cc:
                continue
            s = sum([a, b, c])
            if s > n:
                break
            if s == n:
                yield (a, b, c)
