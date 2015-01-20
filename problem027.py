def euler(n, a=1, b=41):
    return n**2 + a * n + b

# figure out the highest prime result from Euler's formula, below 1000
b, n = max((euler(i),i) for i in range(40) if euler(i) < 1000)
# got b, now shift a to match
# original a = 1, b is element #(n + 1) in the sequence
a = 1 - 2 * (n + 1)

print a * b