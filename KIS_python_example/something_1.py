import math


def main(x):
    result = (x**6/67 -
              66*(math.cos(x))**5)/x + math.sqrt(x**3/28 +
                                                 math.ceil(x)**6)
    return result
