def spiral_sum_diagonals(n):
    if not n % 2:
        raise ValueError('n cannot be even')
    total = 1
    last = 1
    for cycle in xrange(1, (n + 1) / 2):
        for i in range(1, 5):
            last += cycle * 2
            total += last
    return total

print spiral_sum_diagonals(1001)