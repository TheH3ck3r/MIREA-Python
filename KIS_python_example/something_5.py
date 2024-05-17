import math


def main(x):
    n = len(x)
    summary = 0
    for i in range(1, n + 1):
        index = n + 1 - i - 1
        summary += (math.tan(25 + x[index] + ((x[index]) ** 3) / 48)) ** 7
    return summary


def main_2(y, x):
    n = len(x)
    r = 0
    for i in range(1, n+1):
        r += 35 * (abs(x[n - math.ceil(i / 2)] + 63 * y[n - i] ** 2) ** 3)
    return r


if __name__ == '__main__':
    print(main_2([-0.52, -0.42, 0.4, 0.41, -0.3],
                 [0.24, -0.67, -0.97, -0.22, 0.78]))
