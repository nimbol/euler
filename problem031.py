coins = {
    1:  [],
    2:  [(1,1)],
    5:  [(2,2,1)],
    10: [(5, 5), (2, 2, 2, 2, 2)],
    20: [(10, 10)],
    50: [(20, 20, 10)],
    100:[(50, 50), (20, 20, 20, 20, 20)],
    200:[(100, 100)],
}
queue = set([(200,)])
result = set([(200,)])

while queue:
    #pop a combination of coins out of the queue
    curr = queue.pop()

    #find a coin of every denomination in the current set
    for c in coins:
        if c not in curr:
            continue

        # break it down into all its combinations
        for combi in coins[c]:
            copy = list(curr)
            copy.remove(c)
            copy.extend(combi)
            copy = tuple(sorted(copy, reverse=1))
            # prevent adding a known combination to the queue
            if copy not in result:
                #add to the queue (a set) AND to results (a set)
                queue.add(copy)
                result.add(copy)

print len(result)#, sorted(result, reverse=1)