def diffsumsquare(n):
# my brute-force attempt...
#    sq = sum(range(n + 1)) ** 2
#    sm = sum(i ** 2 for i in range(n + 1))
    # mathematical approach:
    sq = ((n * (n + 1)) / 2) ** 2
    sm = (n * (n + 1) * (2 * n + 1)) / 6
    return sq, sm

d = diffsumsquare(100)
print d[0] - d[1], d
