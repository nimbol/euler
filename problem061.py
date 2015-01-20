import figurate_numbers as fn
from collections import defaultdict as ddict

def represents(i):
    '''Checks if the numbers in iterable i represent all polygonal types.'''
    i = set(i)
    alloc = {}
    # Check if all polygonal types are represented in any way.
    for k in coll:
        inter = coll[k].intersection(i)
        if not inter:
            # No number in i represents this polygonal type.
            return False
        alloc[k] = inter
    
    # Check if each polygonal type can be represented by a different number.
    for n8 in alloc[8]:
        for n7 in alloc[7]:
            if n7 == n8: continue
            for n6 in alloc[6]:
                if n6 in (n7,n8): continue
                for n5 in alloc[5]:
                    if n5 in (n6,n7,n8): continue
                    for n4 in alloc[4]:
                        if n4 in (n5,n6,n7,n8): continue
                        for n3 in alloc[3]:
                            if n3 in (n4,n5,n6,n7,n8): continue
                            return True
    return False

coll = ddict(set)
starts = ddict(set)
ends = ddict(set)

functions = {
    3: fn.triangle,
    4: fn.square,
    5: fn.pentagonal,
    6: fn.hexagonal,
    7: fn.heptagonal,
    8: fn.octagonal,
}

# Populate collections.
for key in functions:
    i = 1
    n = functions[key](i)
    while n < 10000:
        if n > 999:
            coll[key].add(n)
            starts[str(n)[:2]].add(n)
            ends[str(n)[2:]].add(n)
        i += 1
        n = functions[key](i)

# Remove numbers that would break the cyclic pattern anyway, causing dead ends.
for obsolete in set(starts).symmetric_difference(set(ends)):
    for c in coll:
        for n in coll[c].copy():
            if str(n).find(obsolete) in (0, 2):
                coll[c].remove(n)
for obsolete in set(starts).difference(set(ends)):
    del(starts[obsolete])
for obsolete in set(ends).difference(set(starts)):
    del(ends[obsolete])

# Make all possible cycles regardless (almost) of polygonal type.
count = 0
n = [None] * 6
for n0 in coll[8]:
    n[0] = n0
    for n1 in (s for s in starts[str(n0)[2:]] if s not in n):
        n[1] = n1
        for n2 in (s for s in starts[str(n1)[2:]] if s not in n):
            n[2] = n2
            for n3 in (s for s in starts[str(n2)[2:]] if s not in n):
                n[3] = n3
                for n4 in (s for s in starts[str(n3)[2:]] if s not in n):
                    n[4] = n4
                    for n5 in (s for s in starts[str(n4)[2:]] if str(s)[2:]==str(n0)[:2] and s not in n):
                        n[5] = n5
                        # Check if all polygonal types are represented.
                        if represents(n):
                            print sum(n), n
                    n[5] = None
                n[4] = None
            n[3] = None
        n[2] = None
    n[1] = None

