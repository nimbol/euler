from urllib import urlopen

cardrank = '23456789TJQKA'
handrank = [
    'high card',
    'pair',
    '2 pair',
    'trips',
    'straight',
    'flush',
    'full house',
    'quads',
    'straight flush',
]
def cardkey(c):
    return cardrank.index(c)

def hand(cards):
    '''
    Determines what poker hand the cards represent.
    Returns an iterable that can be used for comparison against another hand.
    '''
    # check all possible hands, from high ranking to low
    ranks = ''.join(sorted((c[0] for c in cards), key=cardrank.index, reverse=True))
    suits = ''.join(c[1] for c in cards)
    
    if suits.count(suits[0]) == 5:
        # some kind of flush
        if ranks in cardrank[::-1]:
            # straight flush
            return (handrank.index('straight flush'), ranks)
        else:
            # regular flush, no chance of quads / full house
            return (handrank.index('flush'), ranks)
            
    multi = ranks.count(ranks[2])
    if multi == 4:
        # quads
        if ranks[0] != ranks[1]:
            # put quads before spare card
            ranks = ranks[1:] + ranks[0]
        return (handrank.index('quads'), ranks)
        
    if multi == 3:
        # trips or full house
        if len(set(ranks)) == 2:
            # full house
            if ranks[1] != ranks[2]:
                # put trips before pair
                ranks = ranks[2:] + ranks[:2]
            return (handrank.index('full house'), ranks)
        else:
            # trips, no chance of straight; move trips to front
            rank = ranks[2]
            ranks = rank*3 + ranks.replace(rank, '')
            return (handrank.index('trips'), ranks)
            
    if ranks in cardrank[::-1]:
        # straight
        return (handrank.index('straight'), ranks)
        
    if len(set(ranks)) == 3:
        # two pairs; place the odd card at the end
        for r in ranks:
            if ranks.count(r) == 1:
                ranks = ranks.replace(r, '') + r
                return (handrank.index('2 pair'), ranks)
                
    if len(set(ranks)) == 4:
        # pair; move to front
        for r in ranks:
            if ranks.count(r) == 2:
                ranks = r*2 + ranks.replace(r, '')
                return (handrank.index('pair'), ranks)
                
    return (handrank.index('high card'), ranks)

if __name__ == "__main__":
    score = 0

    url = 'http://projecteuler.net/project/poker.txt'
    for line in urlopen(url):
        cards = line.split()
        hands = hand(cards[:5]), hand(cards[5:])
        if hands[0][0] > hands[1][0]:
            score += 1
        elif hands[0][0] == hands[1][0]:
            for i in range(5):
                if hands[0][1][i] == hands[1][1][i]:
                    continue
                if cardrank.index(hands[0][1][i]) > cardrank.index(hands[1][1][i]):
                    score += 1
                break

    print score

