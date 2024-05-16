import math


def main(n):
    if n == 0:
        return 0.04
    elif n == 1:
        return 0.75
    elif n >= 2:
        value = (math.ceil(22 * main(n - 2)) ** 2) / 46 \
                - (math.ceil(main(n - 2))) ** 3\
                - (main(n - 1)) ** 2 / 8
        return value


if __name__ == '__main__':
    print(main(9))
