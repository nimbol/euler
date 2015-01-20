from urllib import urlopen
from itertools import product, imap, cycle
from string import lowercase
from operator import xor

url = 'http://projecteuler.net/project/cipher1.txt'
cipher = [int(i) for i in urlopen(url).read().split(',')]

for passkey in product((ord(l) for l in lowercase), repeat=3):
    text = ''.join(chr(i) for i in imap(xor, cipher, cycle(passkey)))
    if ' the ' in text:
        #print text
        break

print sum(ord(letter) for letter in text)

