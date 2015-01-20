# I see two ways: brute-force, or reverse-apply
# Can't figure out reverse-apply :)
import time
_t = time.time()

def seq_next(n):
    """
    "Where do I get from here?"
    """
    if n % 2:
        return 3 * n + 1
    return n / 2

def rev_seq(n):
    """
    "How did I get here?"
    """
    yield n * 2
    if not ((n - 1) % 3):
        yield (n - 1) / 3

cache = {1: 0}
record = (1, 0)

for i in xrange(2, 1000000):
    seq = []
    while i not in cache:
        seq.append(i)
        i = seq_next(i)
    length = 1
    cached_len = cache[i]
    for n in seq[::-1]:
        cache[n] = length + cached_len
        length += 1
    else:
        if cache[n] > record[1]:
            record = (n, cache[n])

print record
print time.time() - _t
