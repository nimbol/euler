from collections import defaultdict

class Grid(defaultdict):
    """
    Calculates how many routes there are from (x, y) to (0, 0) without backtracking.
    As such each point in the grid is assigned a value which represents the number
    of routes there are from that point.
    """
    def __init__(self):
        defaultdict.__init__(self, dict)

    def get(self, x, y):
        """
        Public method for getting the value of coordinates (x, y) on the grid.
        This will return a known value, or get it calculated if it's unknown.
        """
        try:
            return self[y][x]
        except:
            self[y][x] = self._calc(x, y)
            return self[y][x]

    def _calc(self, x, y):
        """
        Calculates the value for coordinate (x, y).
        The algorithm used calculates only 1/4 of all values in the grid.
        """
        if not (x and y):
            return 1
        if x == y:
            div, mod = divmod(x, 2)
            if not mod:
                return 2 * sum(self.get(div + i, div - i) ** 2 for i in range(1, div + 1)) \
                    + self.get(div, div) ** 2
            else:
                return 2 * sum(self.get(div + 1 + i, div - i) ** 2 for i in range(div + 1))
        else:
            return self.get(x - 1, y) + self.get(x, y - 1)

if __name__ == '__main__':
    g = Grid()
    print g.get(20, 20)
    for y in range(21):
        for x in range(21):
            try:
                g[y][x]
                print 'x',
            except KeyError:
                print ' ',
        print