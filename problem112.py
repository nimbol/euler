from itertools import count

bouncy = set()
target_pct = 99
portion = 'reset'

for n in (str(c) for c in count(100)):
    # check if matched portion from previous n matches this n as well (optimization)
    if portion in n:
        bouncy.add(n)
        continue

    # test portions of n, increasing in size, for known bounciness
    for size in range(3, len(n)):
        for idx in range(len(n) - (size - 1)):

            portion = n[idx:idx+size]

            if portion in bouncy:
                bouncy.add(n)
                break
        else:
            continue
        break
    # test n as a whole, for previously unseen bounciness
    else:
        if portion != 'reset': portion = 'reset'
        compare = {}
        prev = int(n[0])
        for d in (int(c) for c in n[1:]):
            compare[cmp(d, prev)] = True
            try:
                compare[-1]
                compare[1]
                bouncy.add(n)
                break
            except KeyError:
                prev = d

    if str(len(bouncy) * 100 / target_pct) == n:
        break

print n