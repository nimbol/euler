# Observations:
# Sum(n + r) is a number with an EVEN amount of digits!
# Digits at the edges of n are the most significant.
# If n has an odd number of digits, high digits are required to reach a sum
# with an even number of digits (and vv). The middle digit will be summed with
# itself. In 3-digit numbers this implies it cannot exceed 4, because it would
# spill over and make the next digit even.
# Of digits d of n, d[0] and d[-1] must add up to be odd, so one odd one even.
# If d[0]+d[1] > 10 then d[1] and d[-2] must be both odd or even.

# Count just numbers ending in odds and count them double.

import time
T = time.clock()

count = 0
odds = range(1, 10, 2)
evens = range(10, 2)
edge_evens = range(2, 10, 2)

for ndigits in (2, 3):
    # ndigits % 2: start with high digits on outside, low middle digit

print time.clock() - T
