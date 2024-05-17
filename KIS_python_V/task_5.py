import math


def main(z):
    n = len(z)
    res = 0
    for i in range(1, n + 1):
        i_z = z[n - i]
        res += 49 * (math.tan((39 * (i_z ** 3)) - 38 - i_z) ** 6)
    return res


if __name__ == '__main__':
    print(main([0.95, 0.43, -0.19, 0.96, -0.44, 0.66, 0.37]))
    print(main([-0.64, 0.46, -0.23, 0.13, 0.81, -0.42, -0.84]))
    print(main([0.85, 0.15, -0.4, 0.47, -0.01, 0.3, -0.83]))