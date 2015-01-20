from mymath import mul

def factorial(n):
    """
    -> n!
    Don't try this for n > 25 or so. :)
    """
    return mul(xrange(1, n + 1))

def factorial_large(n):
    """
    Should work for any n.
    -> str(n!)
    """
    i = 0
    total = 1
    zeroes = 0
    while i != n:
        i += 1
        total *= i
        while not total % 10:
            total /= 10
            zeroes += 1
    return str(total) + zeroes * '0'

print sum(int(i) for i in factorial_large(100))