#from mymath import smallest_divisible as sd

numbers = '123456789'
collect = []

for n in range(2, 10):
    r = range(1, n + 1)
    div, mod = divmod(9, len(r))
    # An attempt to limit numbers tested;
    # generating them would be smarter, but might be slower.
    if mod:
        start = 10 ** div / r[-mod]
        stop = 10 ** div / r[-mod - 1]
    else:
        start = int(numbers[:div])
        stop = int(numbers[:-div - 1:-1])

    for i in xrange(start, stop + 1):
        p = ''.join(str(i * x) for x in r)
        if ''.join(sorted(p)) == numbers:
            collect.append(int(p))

print max(collect)