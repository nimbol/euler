def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def tribonacci():
    a, b, c = 1, 1, 1
    yield a
    yield b
    while True:
        yield c
        a, b, c = b, c, a + b + c
