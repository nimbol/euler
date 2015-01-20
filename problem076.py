cache = {}
def count_combinations(n, m):
    try:
        return cache[(n, m)]
    except KeyError:
        result = sum(count_combinations(n - i, i) for i in xrange(m, n/2 + 1)) + 1
        cache[(n, m)] = result
        return result

print count_combinations(100, 1) - 1

