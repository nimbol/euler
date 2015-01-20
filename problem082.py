import urllib
from collections import defaultdict

if False:
    matrix = [[int(i) for i in line.split()] for line in \
'''131 673 234 103 18
201 96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37 331'''.split('\n')]

else:
    filename = 'problem081.txt'  # yes, it's the same file as for prob81
    url = 'http://projecteuler.net/project/matrix.txt'
    try:
        f = open(filename)
    except IOError:
        f = open(filename, 'w')
        f.write(urllib.urlopen(url).read())
        f.close()
        f = open(filename)

    matrix = [[int(s) for s in line.split(',')] for line in f]
    f.close()

L = len(matrix)

scores = defaultdict(dict)

# Start out by "computing" the first column.
x = 0
for y in xrange(L):
    scores[x][y] = matrix[y][x]

DEFAULT = 80 * 9999

# Now for the fun part.
for x in xrange(1, L):
    # Default to a right-step.
    for y in xrange(L):  # assuming it's square
        scores[x][y] = matrix[y][x] + scores[x-1][y]
    # Now keep minimizing up/down till the column stops changing.
    while True:
        copy = scores[x].copy()
        for y in xrange(L):
            up = scores[x].get(y-1, DEFAULT)
            down = scores[x].get(y+1, DEFAULT)
            scores[x][y] = min(copy[y], up+matrix[y][x], down+matrix[y][x])
        if copy == scores[x]:
            break

print min(scores[x].values())
