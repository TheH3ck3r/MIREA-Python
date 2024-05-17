import math


def main(z):
    if z < -13:
        return "{:.2e}".format(math.sin(z) ** 5)
    elif -13 <= z < 31:
        return "{:.2e}".format((z ** 6) + 53)
    elif z >= 31:
        return "{:.2e}".format(z ** 2)


if __name__ == '__main__':
    print(main(51))