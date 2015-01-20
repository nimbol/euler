import prime
import itertools

def ndivisors(x):
    '''Returns the number of divisors of x.'''
    try:
        return cache[x]
    except KeyError:
        pass

    result = 1        
    count = 0
    xc = x
    prime = itertools.chain(primes, pgen)
    while xc > 1:
        p = prime.next()
        while xc % p == 0:
            count += 1
            xc /= p
        else:
            if count:
                result = (count + 1) * ndivisors(xc)
                break
    cache[x] = result
    return result

cache = {}
primes = []
pgen = prime.generate_and_store(primes, prime.generate())

if __name__ == '__main__':
    i = 0
    t = 0
    result = 0

    while result <= 500:
        i += 1
        t += i
        result = ndivisors(t)
    else:
        print t

