from collections import defaultdict as ddict

i = 345
target = 5
coll = ddict(list)

while True:
    i += 1
    n = i ** 3
    key = ''.join(sorted(str(n)))
    coll[key].append(n)
    if len(coll[key]) == target:
        break

print coll[key][0]

