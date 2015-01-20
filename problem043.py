import itertools

print sum(
    int(''.join(i))
    for i in itertools.permutations('1234567890')
    if i[3] in '02468'
    and i[5] in '05'
    and not int(''.join(i[2:5])) % 3
    and not int(''.join(i[4:7])) % 7
    and not int(''.join(i[5:8])) % 11
    and not int(''.join(i[6:9])) % 13
    and not int(''.join(i[7:])) % 17
)
