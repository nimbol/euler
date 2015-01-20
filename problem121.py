from itertools import chain, combinations
from mymath import mul

# generate a limited powerset
def powerset(iterable):
    s = list(iterable)
    length = (len(s) // 2) + (len(s) % 2)
    return chain.from_iterable(combinations(s, r) for r in range(length))

rounds = 15
values = range(1, 2 + rounds)

num = sum(mul(s) for s in powerset(values[:-1]))
den = mul(values)
amt = den // num

print '%d (odds of winning: %d / %d => $%d)' % (amt, num, den, amt)
