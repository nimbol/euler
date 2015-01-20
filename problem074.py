from mymath import factorial
from combinatorics import combinations_with_replacement as CWR
from itertools import permutations

def normalize(n):
    """Sorts the digits in n."""
    return int(''.join(sorted(str(n), reverse=True)))

ndigits = 6
digits = range(10)
limit = 10 ** ndigits - 1

# Generate factorials cache for all digits.
facts = dict((str(n), factorial(n)) for n in digits)
#facts = [factorial(n) for n in digits]
del(factorial)

# There's actually no need to test all numbers up to limit. All permutations of
# a number will have the same sum. Convert all numbers to their base permutation
# and multiply the final score to account for this conversion.
path = {}
chains = []
for length in xrange(1, ndigits + 1):
    for perm in CWR(digits[::-1], length):
        # Form an integer first, so that path keys/values are of the same type.
        n = sum(perm[i] * 10**(length -i -1) for i in range(length))
        chain = [n]

        while n not in path:
            # Register factorial sum for n.
            factsum = sum(facts[d] for d in str(n))
            path[n] = factsum
            # Get the next number in the chain and register it.
            n = normalize(factsum)
            chain.append(n)
        else:
            if len(chain) == 1:
                # Got just one number and it's been found before. Nothing to see here.
                continue
            if chain.count(n) > 1:
                # The current chain loops.
                chains.append(chain[:-1])
            else:
                # Found the start of a different chain, add them together.
                for c in chains:
                    try:
                        i = c.index(n)
                    except ValueError:
                        continue
                    if i == 0:
                        # Insert current chain at the start of the found chain.
                        c[:1] = chain
                    else:
                        # Can't insert current chain, make a separate one instead.
                        chain.extend(elem for elem in c[i+1:] if elem not in chain)
                        chains.append(chain)
                    break
                else:
                    raise IndexError('n %d reported found, but not present in chains!' % n)

# Identify chains with length 60.
result = set()
for n in [c[0] for c in chains if len(c)==60]:
    result.update(i for i in permutations(str(n), len(str(n))) if i[0]!='0')

print len(result)#, [''.join(r) for r in result]

