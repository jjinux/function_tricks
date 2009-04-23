"""First-class functions and state machines go hand-in-hand.

Instead of using a string for the name of the state, you can just return
the function itself.

"""


def f1():
    print "Called f1"

    # Don't just call f2.  Instead, return it as the next state.

    return f2


def f2():
    print "Called f2"
    return f3


def f3():
    print "Called f3"
    print "Do you want me to keep going (Y or N)?",
    if raw_input() == 'Y':
        return f1
    else:
        return None


# Each function gets called and returns a new function.  Then, bounce
# "bounces" back into the new function.  Since no recursion is used,
# bounce can keep bouncing into new functions forever without hitting a
# stack overflow.
#
# Conceptually, these are coroutines.  When f1 "calls" f2, conceptually
# it never returns to f1.  f2 isn't a *sub*-routine called by f1.
# Rather, f1, f2, and f3 are *co*-routines that call each other in a
# cycle.

def bounce(state):
    while state is not None:
        state = state()


bounce(f1)
