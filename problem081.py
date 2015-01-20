import urllib
from collections import defaultdict

#matrix = [[int(i) for i in line.split()] for line in \
#'''131 673 234 103 18
#201 96 342 965 150
#630 803 746 422 111
#537 699 497 121 956
#805 732 524 37 331'''.split('\n')]

url = 'http://projecteuler.net/project/matrix.txt'
matrix = [[int(s) for s in line.split(',')] for line in urllib.urlopen(url)]

L = len(matrix)

#scores = defaultdict(dict)
scores = dict()

# Start out by computing easy scores for each axis.
y = 0
for x in xrange(L):
    scores[(x,y)] = sum(matrix[y][:x+1])

x = 0
for y in xrange(L):
    scores[(x,y)] = sum(matrix[i][x] for i in xrange(y + 1))

# Now for the fun part.
for x in xrange(1, L):
    for y in xrange(1, L):
        scores[(x,y)] = matrix[y][x] + min(scores[(x-1,y)], scores[(x,y-1)])

print scores[(L-1,L-1)]
