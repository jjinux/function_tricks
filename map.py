"""First class functions are useful as callbacks."""


def square(x):
    return x * x


ints = range(10)
squares = map(square, ints)
#             ^ callback
#                     ^ list
print "squares:", squares


# You can use a lambda with map.

cubes = map(lambda x: x ** 3, ints)
print "cubes:", cubes


# However, list comprehensions are often more readable.

cubes = [x ** 3 for x in ints]
print "cubes:", cubes
