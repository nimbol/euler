from pyramid import Pyramid
import urllib

p = Pyramid()
s = urllib.urlopen('http://projecteuler.net/project/triangle.txt').read()
p.parse(s)
print p.get_max_path()