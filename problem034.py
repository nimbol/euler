from mymath import factorial
import sys

fact = dict((str(i), factorial(i)) for i in range(10))

def roundup(n):
    """
    Rounds integer n up to the nearest next decimal.
    """
    # figure out denomination d
    d = 1
    while True:
        if n % 10 ** d:
            break
        d += 1
    # use builtin rounding function
    r = int(round(n, -d))
    # if number turns out lower, add 10**d
    if r < n:
        r += 10 ** d
    return r

n = 3
collect = []

while n < fact['9'] * 7:
#    print '\r',n,
#    sys.stdout.flush()
    f = sum(fact[i] for i in str(n))
    if f > n:
        n = roundup(n)
        continue
    elif f == n:
        collect.append(n)
    n += 1

print sum(collect)
