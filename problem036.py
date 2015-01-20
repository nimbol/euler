#brute force: convert all palindrome numbers below 1M to binary and check
#maybe smarter: generate palindrome binaries and convert to decimal
#but this runs fast enough :)

collect = []

for n in xrange(10 ** 6):
    if str(n) == str(n)[::-1]:
        b = bin(n)[2:]
        if b == b[::-1]:
            collect.append(n)

print sum(collect)
