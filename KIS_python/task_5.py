import math


def main(z):
    n = len(z)
    res = 0
    for i in range(n):
        res += (95 * ((24 * z[math.ceil(i / 4)] ** 2) - 99) ** 7)
    return res


if __name__ == '__main__':
    print(main([0.42, 0.64, -0.48, -0.74, -0.9, 0.78]))