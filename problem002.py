from fibonacci import fibonacci

f = fibonacci()
n = 0
total = 0
while n <= 4000000:
    if not n%2:
        total += n
    n = f.next()

print total
