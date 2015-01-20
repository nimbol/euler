result = 0

num, den = 1, 1

for i in xrange(1000):
    num, den = num + 2 * den, num + den
    result += (len(str(num)) > len(str(den)))

print result

