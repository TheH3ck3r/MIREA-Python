import math


def main(n):
    if n == 0:
        return -0.21
    elif n == 1:
        return 0.22
    elif n >= 2:
        value_1 = (math.log(((main(n - 1)) ** 2) + (main(n - 1))) ** 3)
        value_2 = (71 * (main(n - 2)))
        value_3 = ((math.sin(main(n - 2))) ** 2)
        result = value_1 + value_2 + value_3
    return result


if __name__ == '__main__':
    print(main(8))