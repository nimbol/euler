limit = 10**12
const = 3 + 2 * 2 ** 0.5
blue = 84

while True:
    blue += 1
    total = int((2 * blue) / (2 ** 0.5))
    if (total * (total - 1)) % (blue * (blue - 1)) == 0:
#        print total, blue
        if total > limit:
            break
        # The following is a trend I observed in the first few results < 10**6
        blue = int(blue * const) - 3

print blue
