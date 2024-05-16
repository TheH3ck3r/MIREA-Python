import math


def main(n):
    if n == 0:
        return -0.21
    elif n == 1:
        return 0.22
    elif n >= 2:
        value = (math.log(((main(n - 1)) ** 2) + (main(n - 1))) ** 3) \
        + (71 * (main(n - 2))) \
        + ((math.sin(main(n - 2))) ** 2)
    return value


if __name__ == '__main__':
    print(main(8))