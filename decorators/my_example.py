from functools import wraps


def mydecorator(func):
    @wraps(func)  # with @wraps, myfunc.__name__ is 'myfunc'. without @wraps, myfunc.__name__ is is 'wrapped'
    def wrapped(*args, **kwargs):
        print "Before decorating function. keyword args: %s" % kwargs
        return func(injected="huzzah!", *args, **kwargs)

    return wrapped


@mydecorator
def myfunc(injected, myarg):
    print injected
    print myarg


myfunc(myarg='asdf')
# huzzah!
# asdf

print myfunc.__name__
# myfunc
