collect = []

for x in xrange(11, 100):
    if not x % 10:
        continue  # skip multiples of 10 (considered trivial)
    for y in xrange(x + 1, 100):
        div, mod = divmod(y, 10)
        if not mod:
            continue  # skip multiples of 10 (considered trivial)
        if str(div) in str(x):
            overlap = div
        elif str(mod) in str(x):
            overlap = mod
        else:
            continue  # no overlap, skip
        xx, yy = [int(str(i).replace(str(overlap), '', 1)) for i in (x, y)]
        if float(x) / y == float(xx) / yy:
            collect.append((x, y))

#print collect

x, y = 1, 1
for i in collect:
    x *= i[0]
    y *= i[1]

if not y % x:
    print y / x
else:
    print x, '/', y
