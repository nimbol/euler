import urllib
import string

def triangle_gen(cache):
    """Generator for triangle numbers."""
    n = 1
    i = 1
    while True:
        cache.append(n)
        yield n
        i += 1
        n += i

cache = []
tgen = triangle_gen(cache)
tgen.next()

words = urllib.urlopen('http://projecteuler.net/project/words.txt')\
        .read().strip('"').split('","')

result = 0

for word in words:
    score = sum(string.uppercase.index(letter) + 1 for letter in word)
    if score in cache:
        result += 1
        continue
    m = max(cache)
    if m > score:
        continue
    while score > m:
        m = tgen.next()
    if score == cache[-1]:
        result += 1

print result
