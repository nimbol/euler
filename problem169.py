def count_combinations(n):
    """
    Setup function for the recursive _count_combinations().
    """
    code = bin(i)[2:]
    if len(code) < 2:
        return 0
    elif not '0' in code:
        return 1
    else:
        global seen, cache, cache_hits
        seen.clear()
        return _count_combinations(code)

seen = set()  # For skipping codes that have already been done, false positives.

def _count_combinations(code):
    """
    Counts the number of ways a given number can be written as the sum of powers
    of 2. Any element in the sum is allowed to be used at most two times.
    """
    # If this code was already generated on another path, skip it completely.
    if code in seen:
        return 0
    else:
        seen.add(code)  # Make sure it's skipped in the future.

    # Try returning a known value from cache instead of calculating it.
    result = 1

    i = len(code)  # current position in the code
    index = [i] * 3  # keeping track of closest 0, 1, 2; default out-of-range.
    for digit in code[::-1]:
        i -= 1
        digit = int(digit)

        # Skip zeroes or if 1 or 2 occurs before 0 (can't be broken down).
        if index[0] == len(code) or 0 == digit or index[0] != min(index):
            index[digit] = i
            continue
        index[digit] = i

        # Generate new code to pass to count_combinations()
        newcode = code[:i] + str(digit - 1) + '2' * (index[0] - i) + code[index[0] + 1:]
        result += _count_combinations(newcode)

    return result

def f(n):
    code = bin(n)[2:]
    results = []
    add = 1
    
    for L in (len(i) + 1 for i in code.lstrip('0').split('1')[:0:-1]):
        result = L
        try:
            result *= results[-1]
            result += add
            if L > 1:
                add += sum(results[-2:])
        except IndexError:
            # The above will only fail for the first result.
            pass
        results.append(result)
            
    return result

import sys

for code in ('10', '001110', '001010', '101010', '10101010', '1010101010', '101010101010', '11010101010', '111010101010'):
    i = int(code, 2)
#for i in xrange(1, 11):
    #i = 10 ** 25
    #code = bin(i)[2:]
    print i,
    print code,
    sys.stdout.flush()
    print count_combinations(i),
    print f(i)
#    break

