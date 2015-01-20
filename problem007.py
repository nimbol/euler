import prime

gen = prime.generate()
for i in xrange(10000):
    gen.next()

print gen.next()
