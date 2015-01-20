# A triangle whose interior contains (0,0) will cross both axis (x and y) twice,
# once below zero, once above zero.

from fractions import Fraction
from itertools import combinations

def cross(p, q):
    '''
    Determine which axes are crossed by line segment (p, q).
    Returns a list [x, y] with value of x for y=0 and vice versa, or None if
    line section doesn't cross that axis.
    '''
    result = [None, None]
    # Compute the formula "y = ax + b"
    a = Fraction(q[1] - p[1], q[0] - p[0])
    b = a * -q[0] + q[1]

    # Get x for y=0 and vice versa.
    x = Fraction(-b, a)
    y = b

    # See if the segment delimited by p and q actually crosses any axes.
    if p[1] >= 0 >= q[1] or q[1] >= 0 >= p[1]:
        result[0] = x
    if p[0] >= 0 >= q[0] or q[0] >= 0 >= p[0]:
        result[1] = y

    return result

count = 0

filename = 'problem102.txt'
for line in open(filename):
    coords = tuple(int(i) for i in line.split(','))

    # Can skip this line straight away if all dots are on one side of an axis.
    if min(coords[::2]) > 0 or max(coords[::2]) < 0:
        continue
    if min(coords[1::2]) > 0 or max(coords[1::2]) < 0:
        continue

    a, b, c = (coords[i:i+2] for i in range(0, 6, 2))
    track = set(['left', 'right', 'hi', 'lo'])

    for (x, y) in (cross(*combi) for combi in combinations([a, b, c], 2)):
        # If any line crosses (0,0)...
        if 0 in (x, y):
            count += 1  # include it?
            break
        # I had a nice setup which used set().remove() instead of .discard(),
        # but those bastards included one triangle with a point on the axis.
        try:
            if x is not None:
                if x < 0:
                    track.discard('left')
                else:
                    track.discard('right')
            if y is not None:
                if y < 0:
                    track.discard('lo')
                else:
                    track.discard('hi')
        # If any line crosses an axis twice on the same side, give up now.
        except KeyError, e:
            break
    else:
        if not track:
            count += 1

print count
