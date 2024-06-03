import math


def main(x):
    n = len(x)
    res = 0
    for i in range(1, n + 1):
        index_z = (9 * (x[math.ceil(i / 4) - 1])) - 0.01
        res += (math.ceil(index_z) ** 4) / 84
    return res

print(main([0.83, -0.87, -0.33, 0.81, 0.79, 0.63, -0.97]))
print(main([0.66, -0.55, 0.13, -0.72, -0.74, -0.1, -0.06]))