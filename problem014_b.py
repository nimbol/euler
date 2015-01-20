import time
_t = time.time()

collatz = {1:0}

def Collatz(n):
    global collatz
    if not collatz.has_key(n):
        if n%2 == 0:
            collatz[n] = Collatz(n/2) + 1
        else:
            collatz[n] = Collatz((3*n + 1) / 2) + 2
    return collatz[n]

#for j in range(1000000,2,-1):
for j in range(2,1000000):
    Collatz(j)

print collatz.keys()[collatz.values().index(max(collatz.values()))]
print time.time() - _t
