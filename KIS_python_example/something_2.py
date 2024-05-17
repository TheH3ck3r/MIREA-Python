import math


def main(y):
    if y < 96:
        return y ** 3 + y ** 2
    elif 96 <= y < 111:
        return 15 * y ** 7 - (52 * y - y ** 2) ** 6
    elif 111 <= y < 158:
        return 14*y**3 - y**7
    elif 158 <= y < 256:
        return math.fabs(y) ** 2 + 1
    elif y >= 256:
        return y**2/93 + 26*(math.sqrt(y))**4


if __name__ == '__main__':
    print(main(185))
