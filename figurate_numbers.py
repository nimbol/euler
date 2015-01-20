'''
The term figurate number is used by different writers for members of different
sets of numbers, generalizing from triangular numbers to different shapes
(polygonal numbers) and different dimensions (polyhedral numbers).
'''

def triangle(n):
    '''Returns triangle number #n.'''
    return n * (n + 1) / 2

def is_triangle(n):
    '''Checks whether n is a triangle number.'''
    x = (8 * n + 1) ** 0.5
    return x == int(x)

def square(n):
    ''' Returns square number #n.'''
    return n ** 2

def is_square(n):
    ''' Returns square number #n.'''
    x = n ** 0.5
    return x == int(x)

def pentagonal(n):
    '''Returns pentagonal number #n.'''
    return n * (3 * n - 1) / 2

def is_pentagonal(n):
    '''Checks whether n is a pentagonal number.'''
    x = ((24 * n + 1) ** 0.5 + 1) / 6
    return x == int(x)

def hexagonal(n):
    '''Returns hexagonal number #n.'''
    return n * (2 * n - 1)

def is_hexagonal(n):
    '''Checks whether n is a hexagonal number.'''
    x = ((8 * n + 1) ** 0.5 + 1) / 4
    return x == int(x)

def heptagonal(n):
    return n * (5 * n - 3) / 2

def octagonal(n):
    return n * (3 * n - 2)

