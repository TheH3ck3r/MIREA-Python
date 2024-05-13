from contextlib import contextmanager

@contextmanager
def raises(exception):
    try:
        yield
    except exception:
        pass

with raises(ZeroDivisionError):
    1 / 0
