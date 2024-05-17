import math


def main(z):
    top = (83 * (((37 * (z ** 3))) ** 6)) + (96 * (z ** 3))
    bottom = (z ** 7) - (57 * (z ** 6))
    result = (((z ** 2) - 1) + (math.sqrt(top / bottom)))
    return result

if __name__ == "main":
    print(main(-0.01))
    print(main(-0.05))
    print(main(-0.06))