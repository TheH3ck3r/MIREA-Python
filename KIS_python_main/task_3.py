import math


def main(b, m, y):
    sum_1 = 1
    for j in range(1, b + 1):
        sum_1 += (22 * math.log(63 * j**2 - 8 * j)**5 - (j**4 / 36))
    sum_2 = 1
    for k in range(1, m + 1):
        sum_2 += (52 * k**4 - 49 * (math.exp(82 * y + 11 * k**2)**5))
    result = sum_1-sum_2
    return result


if __name__ == '__main__':
    print(main(4, 2, -0.16))