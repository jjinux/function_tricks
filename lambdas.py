"""A lambda is a single expression wrapped in a function."""


def sum(a, b):
    return a + b
print "def:", sum(2, 2)


sum = lambda a, b: a + b
print "named lambda:", sum(2, 2)


print "anonymous lambda:", \
      (lambda a, b: a + b)(2, 2)
#     ^ define it         ^ call it
