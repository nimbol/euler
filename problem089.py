'''Normalizing roman numerals.'''

import urllib

_nummap = dict(
    I = 1,
    V = 5,
    X = 10,
    L = 50,
    C = 100,
    D = 500,
    M = 1000,
)

def sortkey(arg):
    return _nummap[arg]
    
def roman_to_dec(num):
    '''Convert any valid roman numeral to a decimal number.'''
    dec = 0
    prev = 0
    
    for n in num[::-1]:
        i = sortkey(n)
        if cmp(i, prev) < 0:
            dec -= i
        else:
            dec += i
        prev = i
    return dec
    
def roman_from_dec(dec):
    '''Convert any number from the decimal system to roman numerals.'''
    num = ''
    i = dec
    
    # reverse map the roman numerals to decimals
    revmap = dict(zip(_nummap.itervalues(), _nummap.iterkeys()))
    
    # build a non-normalized roman numeral
    for n in sorted(revmap, reverse=True):
        while i >= n:
            num += revmap[n]
            i -= n
    
    # normalize
    num = num \
    .replace('CCCC', 'CD') \
    .replace('XXXX', 'XL') \
    .replace('IIII', 'IV') \
    .replace('DCD', 'CM') \
    .replace('LXL', 'XC') \
    .replace('VIV', 'IX')
    
    return num

oldbytes = 0
newbytes = 0

for num in urllib.urlopen('http://projecteuler.net/project/roman.txt'):
    num = num.strip()
    oldbytes += len(num)
    
    newnum = roman_from_dec(roman_to_dec(num))
    newbytes += len(newnum)

print oldbytes - newbytes, oldbytes, newbytes

