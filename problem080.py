# Calculating sqrt with 100 precision using Babylonian method
# and treating decimals as an integer.

from mymath import precision_div

n = 2
x = repr(n ** .5)
r = ''

while r != x:
    r = x
    
