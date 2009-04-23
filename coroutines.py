"""Generators can be used to create "fake threads"."""


# Each thread does some work and then yields control to another thread.

def thread1():
    while True:
        print "thread1"
        yield


def thread2():
    while True:
        print "thread2"
        yield


def thread3():
    while True:
        print "thread3"
        yield


schedule = [thread1(), thread2(), thread3()]  # Fire up the generators.
while True:
    for thread in schedule:
        thread.next()


# There are limits to this method, however.  thread1 can't easily call some
# other function and let that function do the yield for it.
#
# See: http://jjinux.blogspot.com/2006/08/python-limitations-of-coroutines-via.html
#      http://twistedmatrix.com/trac/
#
# Nonetheless, with a C extension called Greenlet, you can indeed
# achieve a light-weight thread system and have tens of thousands of
# threads at the same time.
#
# See: http://wiki.secondlife.com/wiki/Eventlet
#      http://opensource.hyves.org/concurrence/
#
# These are frameworks for creating massively concurrent network
# applications.
