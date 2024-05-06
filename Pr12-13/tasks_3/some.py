from contextlib import contextmanager


@contextmanager
def raises(exception):
    try:
        yield
    except exception:
        pass


print(type([]) is str)