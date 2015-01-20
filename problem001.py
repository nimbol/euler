#print sum(set.union(set(range(0,1000,3)), set(range(0,1000,5))))

def sum_divisible_by(target, n):
    """
    Sums up everything divisible by n up to and including target.
    """
    sign, n = n / abs(n), abs(n)
    p = target / n
    return sign * n * (p * (p + 1)) / 2

print sum(sum_divisible_by(999, n) for n in (3, 5, - 3 * 5))
