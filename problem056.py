print max(
    sum(
        int(digit)
        for digit in str(a**b)
    )
    for a in xrange(100) 
    for b in xrange(100)
)
