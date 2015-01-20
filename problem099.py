import urllib

best = (1, 1)
i = 1

url = 'http://projecteuler.net/project/base_exp.txt'
for line in urllib.urlopen(url):
    pair = tuple(int(i) for i in line.split(','))
    
    if pair[0] ** (1. / best[1]) > best[0] ** (1. / pair[1]):
        best = pair
        result = i

    i += 1

print result
