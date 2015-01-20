from itertools import permutations

# Find the chain with the highest arbitrarily chosen value (in this case:
# start with the lowest number on the outer ring, listing groups clockwise).
# Limitations:
# Groups have size 3 (this is hardcoded, since it's the same for any size puzzle).
# Every group must add up to the same number, and intersect with 2 others.
# Size of the puzzle, in groups. Max n can be derived from this.
# All fields must get a unique number, from 1 to n.
# Highest scoring puzzle: make sure all the low numbers are in the center.
# Solution's number of digits: if 10 intersects then the solution is longer.

size = 3
maxn = size * 2

for total in xrange(1 + 2 + maxn, 1 + 2 * maxn):
    # All permutations for length-3 groups using numbers 1 - maxn.
    # First number in a tuple goes on the outer ring, the other two are inner.
    # Last number intersects with the next clockwise number.
    perm = tuple(c for c in permutations(xrange(1, maxn + 1), 3) if sum(c)==total and c[0] > size)

    print total, perm