import math


def main(y):
    top = (12 * (y ** 6)) + (78 * ((math.sqrt(77 * (y ** 2))) ** 4))
    bottom = ((math.atan((y ** 3) + (61 * y))) ** 6) - (y ** 2)
    result = (y ** 3) + (59 * (math.exp(45 * y) ** 7)) \
        + (math.sqrt(top / bottom))
    return result

if __name__ == '__main__':
    print(main(-0.63))
    print(main(0.8))
    print(main(-0.84))