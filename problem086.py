def is_square(x):
    return x == int(x**.5) ** 2

r = 0
M = 0

#while r <= 10 ** 6:
while M < 100:
    M += 1
    ab = 2
    while ab <= 2*M:
        if is_square(M**2 + ab**2):
            if ab > M+1:
                r += M + 1 - (ab + 1)/2
            else:
                r += M / 2
        ab += 1

print M, r
