limit = 2 * 10 ** 6

# generate all triangle numbers up to limit
triangle = []
i = t = 0
while t <= limit:
    triangle.append(t)
    i += 1
    t += i

# multiply pairs of triangle numbers and keep track of the closest to limit
left = 1
right = len(triangle) - 1

result = ()
diff = limit

while left <= right:
    prod = triangle[left] * triangle[right]

    # let's be stubborn and see if the perfect solution exists anyway
    if prod == limit:
        result = (left, right)
        break

    # check if the current result improves the score
    d = abs(limit - prod)
    if d < diff:
        diff = d
        result = (left, right)

    # if product exceeds limit, pick a smaller triangle number to multiply with
    # and vice versa
    if prod > limit:
        right -= 1
    else:
        left += 1

print result[0] * result[1], result