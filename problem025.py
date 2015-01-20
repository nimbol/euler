from fibonacci import fibonacci

f = fibonacci()
i = 0
n = 0

while n / 10**999 == 0:
    i += 1
    n = f.next()

print i
