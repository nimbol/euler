threshold = float(15499) / 94744

primes = (3, 5, 7, 11, 13, 17, 19, 23, 27, 31, 37) # more than we need :)

d = 2  # denominator d, from the example
Rd = 1 # resilience of d
copy = {}  # workspace

for p in primes:
    copy['d'] = d
    copy['Rd'] = Rd

    for i in xrange(1, p - 1):
        d += copy['d']
        Rd += copy['Rd']
#        print d, Rd
        if float(Rd) / (d - 1) < threshold:
            break
    else:
        d += copy['d']
#        print d, Rd
        if float(Rd) / (d - 1) < threshold:
            break
        continue
    break

print d
