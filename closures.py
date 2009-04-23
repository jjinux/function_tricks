"""A closure is a function that brings along some state with it."""


# Functions can be nested.

def greeter(name):

    # Notice that greet has access to name.

    def greet():
        print "Hello,", name

    greet()


greeter('Chuck')


# The inner function continues to have access to outer variables even
# after the outer function finishes.

def greeter(name):

    def greet():
        print "Hello,", name

    return greet


jj_greeter = greeter('JJ')
glen_greeter = greeter('Glen')


# greeter is long gone, but jj_greeter still has access to name.

jj_greeter()
glen_greeter()

# jj_greeter is a function, but behind the scenes it's also an object
# with some local state and it responds to one method called __call__.

print "closure:", jj_greeter.func_closure
jj_greeter.__call__()
