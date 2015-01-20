# Evaluate the sum of all the amicable numbers under 10000.
# create a set with all numbers < 10k
# pop a number out, calculate its sum of divisors, pop that number out
# this could easily be optimized by removing all primes from the todo first

from mymath import divisors

def divsum(n):
    return sum(divisors(n) - n)

todo = set(xrange(10000))
collect = []
n = todo.pop()
d = divsum(n)

while todo:
    dd = divsum(d)
    if dd == n and d != n:
        # found a pair
        # this eliminates both numbers, so pick a brand new one while you're at it
        collect.append(n) # save found amicable number
        n = todo.pop()    # get new n from todo list
        d = divsum(n)
        try:
            todo.remove(d)
            collect.append(d)
        except KeyError:
            pass # save d only if it's < 10k
    else:
        try: # make d the new n
            todo.remove(d)
            n = d
            d = dd
        except KeyError: # except if d is not on our todo list
            n = todo.pop()
            d = divsum(n)

print collect
print sum(collect)