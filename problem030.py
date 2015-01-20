def powerize(n, p):
    """
    Returns sum(d**p) where d is each digit of p.
    """
    return sum(int(d)**p for d in str(n))

p = 5

# For completeness' sake let's determine the max n to check here.
d = 1
while d * 9 ** p > 10 ** (d - 1):
    max = d * 9 ** p
    d += 1

# Now that we have a more or less sane maximum, test all numbers up to that.
# Of course generating the tested numbers in a smarter way would speed this up.
# This exercise treats numbers as strings, they should be generated as such too.

total = 0
n = 1
while n <= max:
    n += 1
    r = powerize(n, p)
    if n == r:
        total += r

print total