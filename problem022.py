import urllib
import string

names = sorted(
    urllib.urlopen('http://projecteuler.net/project/names.txt')\
    .read().strip('"').split('","')
)
total = 0
position = 0
for name in names:
    score = 0
    position += 1
    for letter in name:
        score += string.ascii_uppercase.index(letter) + 1
    total += score * position

print total