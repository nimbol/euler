'''
How many Lychrel numbers are there below ten-thousand?
'''

limit = 10000
R = range(1, limit)
result = []

while R:
    # pick the next value < limit
    n = R[0]
    streak = []
    # apply reverse/add up to 50 times, after that we're allowed to assume it's a hit
    for i in xrange(50):
        streak.append(n)
        try:
            R.remove(n)
        except ValueError:
            pass
        n += int(str(n)[::-1])
        if n < limit and n not in R:
            if n in result:
                result.extend(streak)
            break
        if str(n) == str(n)[::-1]:
            break
    else:
        result.extend([s for s in streak if s < limit])

print len(result)#, sorted(result)
