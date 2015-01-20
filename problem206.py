# Since the pattern ends on 0, we know its root must as well. Any root that ends
# on 0 will result in a square that ends on 00. That means we can simplify the
# pattern! Just don't forget to add the 0 when printing the result. :)

from itertools import cycle

pattern = '1_2_3_4_5_6_7_8_9'
lower = int(int(pattern.replace('_', '0')) ** 0.5)
#upper = int(int(pattern.replace('_', '9')) ** 0.5)

# Now we have a pattern that ends on 9. So our root ends on 3 or 7.
i = cycle([4, 6])
n = lower / 10 * 10 + 3

while str(n**2)[::2] != '123456789':
    n += i.next()

print n * 10, n**2 * 100