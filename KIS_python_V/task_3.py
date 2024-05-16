import math


def main(a, b, n):
    sum_1 = 1
    for k in range(1, n + 1):
        sum_2 = 0
        for j in range(1, b + 1):
            sum_3 = 0
            for c in range(1, a + 1):
                sum_3 += (76*((math.floor((64*k)-0.02-(j**3)))**6)) \
                      - (j ** 3) - ((60 * (c ** 3)) ** 2)
            sum_2 += sum_3
        sum_1 *= sum_2
    return sum_1

if __name__ == '__main__':
    print(main(3, 2, 2))
    print(main(3, 7, 4))
    print(main(3, 8, 5))
