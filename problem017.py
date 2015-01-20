english = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}

def int2word(i, langdef=english):
    try:
        if i not in (100, 1000):
            return langdef[i]
    except KeyError:
        pass
    if not i / 100:
        #numbers 1-99
        return langdef[(i / 10) * 10] + langdef[i % 10]  # yes, hyphen dropped
    if not i / 1000:
        #numbers 100-999
        high, low = divmod(i, 100)
        s = langdef[high] + langdef[100]
        if low:
            s += 'and' + int2word(low, langdef) # yes, spaces dropped
        return s
    if not i / 1000000:
        #numbers 1000-999999
        high, low = divmod(i, 1000)
        s = int2word(high, langdef) + langdef[1000]
        if low:
            s += int2word(low, langdef) # yes, spaces dropped
        return s

if __name__ == "__main__":
    print len(''.join(int2word(i) for i in xrange(1, 1001)))