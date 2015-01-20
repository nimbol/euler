class Pyramid(list):
    def __init__(self, string=''):
        """
        Initialize the new pyramid. Optionally pass a string for parsing.
        """
        self.parse(string)

    def get_depth(self, position):
        """
        Returns the number of steps through the pyramid from a certain depth.
        -> int
        """
        try:
            return self.length - position
        except AttributeError:
            self.length = len(self)
            return self.length - position

    def parse(self, string):
        """
        Parses a string that represents the pyramid.
        """
        del self[:]
        for line in string.split('\n'):
            if line:
                self.append([int(i) for i in line.split()])

    def get_max_path(self):
        """
        Calculates the path through the fields that give the maximum sum.
        Returns the sum of those fields.
        -> int
        """
        prev = self[0]  # keep track of running totals (special-cased the top row)
        for next in self[1:]:  # traverse a copy of the pyramid top-to-bottom
            next[0] += prev[0]  # special-case extreme left cell
            next[-1] += prev[-1]  # special-case extreme right cell
            for x in range(1, len(next) - 1):  # traverse the remaining cells by index
                next[x] += max(prev[x + i] for i in (-1, 0))  # add the highest of the possible two paths
            prev = next  # store the running totals
        return max(prev)
